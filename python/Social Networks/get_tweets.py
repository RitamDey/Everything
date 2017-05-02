from tweepy import Cursor


client = make_client()
for status in Cursor(client.home_timeline).items(10):
    print(status.text)
