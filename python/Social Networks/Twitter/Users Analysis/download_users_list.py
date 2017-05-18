from os import makedirs
from sys import argv, exit
import json
import time
from math import ceil
from tweepy import Cursor
from make_client import make_client

MAX_FRIENDS = 15000


def usage():
    print("Usage:")
    print("python {} <username>".format(argv[0]))


def paginate(items, n):
    """
    Generate n-sized chunks for items
    """

    for i in range(0, len(items), n):
        yield items[i:i + n]


if __name__ == "__main__":
    if len(argv) != 2:
        usage()
        exit(1)

    screen_name = argv[1]
    client = make_client()

    dirname = "users/{}".format(screen_name)
    max_pages = ceil(MAX_FRIENDS / 5000)

    try:
        makedirs(dirname, exist_ok=True)
    except OSError:
        print("Can't create directory {}".format(dirname))
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)

    # get followers for a given user
    # fname = "users/{}_followers.json".format(screen_name)
    # with open(fname, 'w') as f:
    #     for followers in Cursor(client.followers_ids, screen_name=screen_name).pages(max_pages):
    #         for chunk in paginate(followers, 100):
    #             users = client.lookup_users(user_ids=chunk)
    #             for user in users:
    #                 print("Getting {}".format(user.name))
    #                 f.write(json.dumps(user._json) + "\n")
    #         if len(followers) == 5000:
    #             print("Sleeping for 60 seconds.")
    #             time.sleep(60)

    # gets friends for a given user
    fname = "users/{}_friends.json".format(screen_name)
    with open(fname, 'w') as f:
        for friends in Cursor(client.friends_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(friends, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    print("Getting {}".format(user.name))
                    f.write(json.dumps(user._json) + "\n")
            if len(friends) == 5000:
                print("Sleeping for 60 seconds.")
                time.sleep(60)

    # get user's profile
    fname = "users/{}_user_profile.json".format(screen_name)
    with open(fname, 'w') as f:
        profile = client.get_user(screen_name=screen_name)
        f.write(json.dumps(profile._json, indent=4))
