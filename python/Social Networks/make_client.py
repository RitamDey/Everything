from tweepy import API
from tweepy import OAuthHandler
import os


def make_client(auth_client=False):
    consumer_key = os.environ["CONSUMER_KEY"]
    access_key = os.environ["ACCESS_KEY"]
    consumer_secret = os.environ["CONSUMER_SECRET"]
    access_secret = os.environ["ACCESS_SECRET"]

    # Setup a OAuth Handler with keys
    client = OAuthHandler(consumer_key, consumer_secret)
    client.set_access_token(access_key, access_secret)

    if auth_client:
        return client

    # Get the client using the OAuth handle created
    client = API(
        client,
        compression=True,
        wait_on_rate_limit=True,
        wait_on_rate_limit_notifyy=True
    )

    # Return it
    return client
