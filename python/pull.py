from selenium.webdriver import Firefox
import subprocess
from json import loads
import time


video_list = loads(open("vids.json").read())
driver = Firefox()


for video in video_list:
    print(video["video_id"])
    driver.get(video['url'])
    url = driver.find_element_by_xpath("//video").get_attribute("src")
    print(url)
    subprocess.run(["wget", "-O", video["video_id"]+".mp4", url])
    time.sleep(5)

