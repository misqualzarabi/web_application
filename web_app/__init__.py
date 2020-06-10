from flask import Flask

from web_app.models2 import db, migrate

from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.twitter_routes import twitter_routes
#from web_app.routes.book_routes import book_routes
#DATABASE_URI = "sqlite:///web_app_pt5.db" # using relative filepath 
DATABASE_URI = "sqlite:///tweet_data.db"

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tweet_routes)
    app.register_blueprint(twitter_routes)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)   