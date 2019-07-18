from re import findall
import subprocess
import requests


NAME_REGEX = r"(?P<name><h2.*)"
VIDEO_REGEX = r"<source.*480.*>"
URL_REGEX = r"https.*\.mp4"

html = requests.get("https://www.erome.com/a/ywy7azfA").text
video = []
url = []

for i in findall(NAME_REGEX, html):
    video.append(i.split(">")[1].strip("</h2")+ ".mp4")


for count, i in enumerate(findall(VIDEO_REGEX, html)):
    if count%2:
        url.append(findall(URL_REGEX, i)[0])
    count += 1

for i,j in zip(video, url):
    subprocess.call(["wget", "--no-clobber", "--continue", "-O", i, j])

