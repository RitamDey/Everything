import os
import json
import facebook
from argparse import ArgumentParser


def get_parser():
    parser = ArgumentParser()
    parser.add_argument('--page')
    return parser


parser = get_parser()
args = parser.parse_args()


token = os.environ.get('FACEBOOK_TOKEN')
fields = ','.join([
        'id',
        'name',
        'about',
        'likes',
        'website',
        'link'
])

graph = facebook.GraphAPI(token)
page = graph.get_object(args.page, fields=fields)

print(json.dumps(page, indent=2))
