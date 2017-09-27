from os import environ  # For getting the token from the shell environment
from json import dumps  # For dumping the returned JSON data
from facebook import GraphAPI  # Actual API


token = environ.get('FACEBOOK_TEMP_TOKEN')
graph = GraphAPI(token)

# Only give me imformation about name and location from profile
profile = graph.get_object('me', fields="name,location")

print(dumps(profile, indent=2))
