from lxml.html import fromstring as etree_fromstring
import requests
from argparse import ArgumentParser
from pathlib import Path
from os import chdir
import pprint

parser = ArgumentParser()
parser.add_argument("url", type=str, help="Url of the Erome Playlist")
parser.add_argument("-f", "--folder", help="Download path", default=Path.cwd(), type=Path)
arguments = parser.parse_args()

if arguments.folder.exists() and arguments.folder.is_dir():
    chdir(arguments.folder)

page = requests.get(arguments.url).text
etree = etree_fromstring(page)
video = {}

for videos in etree.xpath("//div[@class='media-group']"):
    name = videos.xpath("./div[@class='media-details']/h2/text()")[0]
    video_url = videos.xpath("./div[@class='video']/video/source/@src")[0]
    video_format = videos.xpath("./div[@class='video']/video/source/@res")[0]
    video[name] = {}
    video[name]["url"] = video_url
    video[name]["format"] = video_format

pprint.pprint(video)
