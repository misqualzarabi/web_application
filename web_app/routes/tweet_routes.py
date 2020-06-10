from flask import Blueprint, jsonify, request, render_template #, flash, redirect
 
from web_app.models2 import db, Tweet, parse_records

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/tweet.json")
def list_tweets():
    #tweets = [
        #{"id": 1, "tweet": "Tweet 1", "name":"Jeff"},
        #{"id": 2, "tweet": "Tweet 2", "name":"Elon"},
    #]

    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return jsonify(tweets)

@tweet_routes.route("/tweets")
def list_tweets_for_human():
    #tweets = [
        #{"id": 1, "tweet": "Tweet 1", "name":"Jeff"},
        #{"id": 2, "tweet": "Tweet 2", "name":"Elon"},
    #]
    tweet_records = Tweet.query.all()
    print(tweet_records)
    tweets = parse_records(tweet_records)
    return render_template("tweet.html", message="Here's some tweets", tweets=tweets)

@tweet_routes.route("/tweet/new")
def new_tweet():
    return render_template("new_tweet.html") 

@tweet_routes.route("/tweet/create", methods=["POST"])
def create_tweet():
    print("FORM DATA:", dict(request.form))
    # todo: store in database

    new_tweet = Tweet(tweet=request.form["tweet"], user_name=request.form["name"])
    db.session.add(new_tweet)
    db.session.commit()
