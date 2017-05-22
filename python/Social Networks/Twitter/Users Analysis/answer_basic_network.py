import json
import sys


def usage():
    print("Usage:")
    print("python {} <username>".format(argv[0]))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    screen_name = sys.argv[1]
    followers_file = 'users/{}_followers.json'.format(screen_name)
    friends_file = 'users/{}_friends.json'.format(screen_name)

    with open(followers_file) as f1, open(friends_file) as f2:
        followers = set()
        friends = set()
        for line in f1:
            profile = json.loads(line)
            followers.add(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends.add(profile['screen_name'])

    mutual_friends = friends.intersection(followers)
    followers_not_following = followers.difference(friends)
    friends_not_following = friends.difference(followers)

    print("{} has {} followers".format(screen_name,
                                       len(followers)))
    print("{} has {} friends".format(screen_name, len(friends)))
    print("{} has {} mutual friends".format(screen_name,
                                            len(mutual_friends)))
    print("{} friends are not following {} back".format(
        len(friends_not_following), screen_name))
    print("{} followers are not followed back by {}".format(
        len(followers_not_following), screen_name))
