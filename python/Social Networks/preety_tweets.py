from make_client import make_client
from tweepy import Cursor
from sys import argv
import tweepy


try:
    tweets = argv[1]
except IndexError:
    tweets = 10


client = make_client()
for page in Cursor(client.home_timeline, count=tweets).pages(tweets):
    for tweet in page:
        if tweet.retweeted:
            print("{} retweeded".format(tweet.author.name))
        else:
            print("{} tweeted".format(tweet.author.name))
        print("\t{}".format(tweet.text))
        print(tweet.created_at)
