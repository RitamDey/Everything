import json
from sys import argv
from tweepy import Cursor
from make_client import make_client


client = make_client()
username = argv[1]

with open("tweets.json", "w+") as fout:
    curr = Cursor(client.user_timeline, screen_name=username, count=10)
    for page in curr.pages(10):
        for tweet in page:
            fout.write(json.dumps(tweet._json))
