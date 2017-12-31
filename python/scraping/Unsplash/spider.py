import requests
from PIL import Image
from io import BytesIO
from urllib.robotparser import RobotFileParser
from json import load
from os.path import exists
import logging


robots = RobotFileParser()
robots.set_url("https://www.unsplash.com/robots.txt")
robots.read()
logging.basicConfig(
            format="%(asctime)s %(message)s",
            datefmt="%Y-%m-%d %I:%M:%S %p",
            level=logging.DEBUG
        )


start_url = "https://unsplash.com/napi/feeds/home"
next_page = start_url
with open("/home/stux/headers.json") as fout:
    headers = load(fout)


while next_page:
    logging.debug("Fetching %s" %next_page)
    data = requests.get(next_page, headers=headers).json()
    next_page = data.get('next_page', None)

    for pic in data.get('photos', []):
        if exists(pic['id']+".jpeg"):
            logging.info("%s already exists" %(pic['id']+".jpeg"))
            continue
        logging.debug("Fetching %s" %pic['id'])
        pic_data =  requests.get(pic['urls']['full'])
        pic_data = Image.open(BytesIO(pic_data.content))
        logging.info("Saving picture %s" %(pic['id']+".jpeg"))
        pic_data.save(pic['id']+".jpeg", "JPEG")

