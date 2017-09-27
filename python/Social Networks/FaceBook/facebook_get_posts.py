import os
import json
import facebook
import requests


api = facebook.GraphAPI(os.environ.get("FACEBOOK_TOKEN"))
posts = api.get_connections('me', 'posts')

f = open('my_posts.jsonl', 'w+')

while True:
    try:
        for post in posts['data']:
            f.write(json.dumps(post)+"\n")
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break

