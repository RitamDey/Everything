from lxml.html import fromstring as etree_fromstring
import requests
from argparse import ArgumentParser
from pathlib import Path
from os import chdir
from sys import exit
import pprint
import subprocess

parser = ArgumentParser()
parser.add_argument("url", type=str, help="Url of the Erome Playlist")
parser.add_argument("-f", "--folder", help="Download path", default=Path.cwd(), type=Path)
arguments = parser.parse_args()

if arguments.folder.exists() and arguments.folder.is_dir():
    chdir(arguments.folder)
else:
    print("Destination not found")
    exit(1)

page = requests.get(arguments.url).text
etree = etree_fromstring(page)
video = {}

for videos in etree.xpath("//div[@class='media-group']"):
    name = videos.xpath("./div[@class='media-details']/h2/text()")
    if name:
        name = name[0]  # Get the first entry, which should be the media name
    else:
        name = videos.xpath("./@id")[0]
    
    # Check for the avaliable for format and download the highest one
    video_format = videos.xpath("./div[@class='video']/video/source/@res")[0]
    video_url = ""
    if "1080" in video_format:
        video_url = videos.xpath("./div[@class='video']/video/source[@res=1080]/@src")[0]
    else:
        video_url = videos.xpath("./div[@class='video']/video/source/@src")[0]

    video[name] = {}
    video[name]["url"] = video_url
    video[name]["format"] = video_format

pprint.pprint(video)

for vid in video:
    subprocess.call(["/usr/bin/wget", "-O", vid+".mp4", video[vid]["url"]])
