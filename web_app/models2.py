from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class Tweet(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(128))
    user_name = db.Column(db.String(128))

    def __repr__(self):
        return f"<Tweet {self.user_id} {self.tweet} {self.user_name}>"
    
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            tweets = [
        {"user_id": 1, "tweet": "Tweet 1", "user_name":"Jeff"},
        {"user_id": 2, "tweet": "Tweet 2", "user_name":"Elon"},
    ]
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
        return parsed_records