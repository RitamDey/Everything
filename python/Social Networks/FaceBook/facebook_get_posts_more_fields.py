from os import environ
from json import dumps
import facebook as fb
import requests


api = fb.GraphAPI(environ.get("FACEBOOK_TOKEN"))
fields = ",".join([
    'message',
    'created_time',
    'description',
    'caption',
    'link',
    'place',
    'status_type'
])
posts = api.get_connections('me', 'posts', fields=fields)
f = open('my_posts.jsonl', 'w+')


while True:
    try:
        for post in posts['data']:
            f.write(dumps(post)+"\n")
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break

