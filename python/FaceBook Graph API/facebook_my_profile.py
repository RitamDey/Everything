import os
import json
import facebook

token = os.environ.get('FACEBOOK_TEMP_TOKEN')
graph = facebook.GraphAPI(token)
profile = graph.get_object('me', fields='name, location')

print(json.dumps(profile, indent=4))
