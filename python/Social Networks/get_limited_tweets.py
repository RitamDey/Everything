import json
from tweepy import Cursor
from get_tweets import make_client


client = make_client()


with open("tweets.json", "w+") as fout:
    # Get 4 pages of tweets each containing 10 tweets
    for page in Cursor(client.home_timeline, count=10).pages(4):
        for tweet in page:
            fout.write(json.dumps(tweet._json))

