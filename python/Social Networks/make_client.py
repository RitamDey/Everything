from tweepy import API
from tweepy import OAuthHandler
import os


def make_client() -> API:
    consumer_key = os.environ["CONSUMER_KEY"]
    access_key = os.environ["ACCESS_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_secret = os.environ["ACCESS_SECRET"]

    # Setup a OAuth Handler with keys
    client = OAuthHandler(consumer_key, consumer_secret)
    client.set_access_token(access_key, access_secret)

    # Get the client using the OAuth handle created
    client = API(client)

    # Return it
    return client
