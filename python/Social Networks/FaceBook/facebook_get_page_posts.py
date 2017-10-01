import os
import json
import facebook
import requests
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('--page')
parser.add_argument('--n', default=100, type=int)
args = parser.parse_args()


token = os.environ.get('FACEBOOK_TOKEN')
graph = facebook.GraphAPI(token)


all_fields = ','.join([
    'id',
    'message',
    'created_time',
    'shares',
    'likes.summary(true)',
    'comments.summary(true)'
])
posts = graph.get_connections('PacktPub', 'posts', fields=all_fields)


downloaded = 0
while True:  # keep paging
    if downloaded >= args.n:
        break
    try:
        fname = "posts_{}.jsonl".format(args.page)

        with open(fname, 'a+') as f:
            for post in posts['data']:
                downloaded += 1
                f.write(json.dumps(post)+"\n")
            # get next page
            posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break

