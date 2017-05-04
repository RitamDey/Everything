from tweepy import Cursor
from make_client import make_client


client = make_client()
for status in Cursor(client.home_timeline).items(10):
    print(status.text)
