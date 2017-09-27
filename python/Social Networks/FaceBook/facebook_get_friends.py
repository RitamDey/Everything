from os import environ
from facebook import GraphAPI
import json


graph = GraphAPI(environ.get("FACEBOOK_TOKEN"))
user = graph.get_object("me")
friends = graph.get_connections(user["id"], "friends")
print(json.dumps(friends, indent=2))
