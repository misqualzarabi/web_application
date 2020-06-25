from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import openaq


app = Flask(__name__)
api = openaq.OpenAQ()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///air_data_99.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def _finditem(obj, key):
    result = []
    if key in obj: return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = _finditem(v, key)
            if item is not None:
                result.append(item)
                return result[0]



status, body = api.measurements(city='Los Angeles', parameter='pm25')
results = body['results']

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(25))
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Time {} --- Value {}>'.format(self.datetime, self.value)

@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    db.drop_all()
    db.create_all()
    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body['results']
    # url = "https://api.openaq.org/v1/measurements?city=Los%20Angeles&parameter=pm25"
    # response = urllib.request.urlopen(url)
    # reader = codecs.getreader("utf-8")
    # obj = json.load(reader(response))
    # datetime_stuff = _finditem(obj, "utc")
    datetime_stuff = []

    for dictionary in results:
        print(type(dictionary))
        for key, value in dictionary.items():
            # print(key, value)
            print(key, value)
            datetime_stuff_utc = _finditem(dictionary, "utc")
            datetime_stuff_value = _finditem(dictionary, "value")
            if not tuple([datetime_stuff_utc, datetime_stuff_value]) in datetime_stuff:
                datetime_stuff.append(tuple([datetime_stuff_utc, datetime_stuff_value]))
            continue
    for j, k in datetime_stuff:
        print(j,k) 
           
    
        r = Record(datetime=j, value=k)
        db.session.add(r)
    db.session.commit()
    return 'Data refreshed!'

@app.route('/')
def root():
    data = Record.query.filter(Record.value > 10).all()
    print(data)
    display = []
    for d in data:
        print(d)
        print(d.value)
        display.append(tuple([d.datetime, d.value]))
    
    return str(display)
      






   









    
