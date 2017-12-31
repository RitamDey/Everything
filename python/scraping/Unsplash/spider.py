import requests
from PIL import Image
from io import BytesIO
from urllib.robotparser import RobotFileParser
from json import load
from os.path import exists


robots = RobotFileParser()
robots.set_url("https://www.unsplash.com/robots.txt")
robots.read()


start_url = "https://unsplash.com/napi/feeds/home"
seen_photos = set()
next_page = start_url
with open("/home/stux/headers.json") as fout:
    headers = load(fout)


while next_page:
    print("Fetching", next_page)
    data = requests.get(next_page, headers=headers).json()
    next_page = data.get('next_page', None)

    for pic in data.get('photos', []):
        if pic['id'] in seen_photos or exists(pic['id']+".jpeg"):
            continue
        print("Fetching", pic['id'])
        pic_data =  requests.get(pic['urls']['full'])
        pic_data = Image.open(BytesIO(pic_data.content))
        print("Saving picture", pic['id'])
        pic_data.save(pic['id']+".jpeg", "JPEG")
        seen_photos.add(pic['id'])

