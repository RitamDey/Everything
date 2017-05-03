from collections import Counter
from argparse import ArgumentParser
from tweepy import Cursor
from make_client import make_client


def get_hashtags(tweet: dict) -> list:
    """
    The tweet argument is a dict. So get 'entities' key or return a empty dict.
    This is required for the second .get() to not throw a error where we try to
    get 'hashtags'
    """
    entities = tweet.get('entities', {})
    hashtags = entities.get('hashtags', [])

    return ["#" + tag['text'] for tag in hashtags]


def main():
    hashtags = Counter()
    args = ArgumentParser()
    args.add_argument(
        "username",
        help="username of the profile to parse"
    )
    args = args.parse_args()

    client = make_client()
    curr = Cursor(client.user_timeline, screen_name=args.username, count=10)

    for page in curr.pages(10):
        for tweet in page:
            hashtags.update(get_hashtags(tweet._json))

    print(hashtags.most_common(20))


if __name__ == "__main__":
    main()
