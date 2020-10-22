from lxml.html import fromstring as etree_fromstring
import requests
from argparse import ArgumentParser
from pathlib import Path
from os import chdir
from sys import exit
from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import pprint
import subprocess


def scrape_album(url, name, verbosity):
    # Scrape a particular page and fetch all the video links in a dictionary, along with their names and format
    page = requests.get(url).text
    etree = etree_fromstring(page)
    video = {}
    video_count = {"1080": 0, "480": 0}

    print(f"Crawling {name}", end="\t")

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
            video_count["1080"] += 1
        else:
            video_url = videos.xpath("./div[@class='video']/video/source/@src")[0]
            video_count["480"] += 1

        video[name] = {}
        video[name]["url"] = video_url
        video[name]["format"] = video_format

    print(f'Found {video_count["480"]} SD videos and {video_count["1080"]} HD videos. Total {video_count["1080"] + video_count["480"]}')
    
    return video


def scrape_page(url, verbosity):
    # Scrape each individual page and find the albums to download and sends it off for the videos to be extracted
    page = requests.get(url).text
    etree = etree_fromstring(page)
    albums_count = 0
    videos = {}
    
    with ThreadPoolExecutor(max_workers=None) as executor:
        scraping_futures = []
        for album in etree.xpath("//div[@id='albums']/div"):
            albums_count += 1
            title = album.xpath("./a/div/text()")[0].rstrip()
            url = album.xpath("./a/@href")[0]
            scraping_futures.append(executor.submit(scrape_album, url, title, verbosity))

        wait(scraping_futures)
        for future in as_completed(scraping_futures):
            videos.update(future.result())
    
    print(f"{url} has {albums_count} albums")
    return videos


def scrape_profile(url, verbosity):
    # Scrape a user's profile and fetch all it's albums.
    page = requests.get(url).text
    etree = etree_fromstring(page)
    albums = {}
    
    pages = etree.xpath("//ul[@class='pagination']/li")
    pages = int(pages[-2].xpath("./a/text()")[0])
    print(f"Total pages {pages}")
    
    with ThreadPoolExecutor(max_workers=None) as executor:
        scraping_futures = [executor.submit(scrape_page, f"{url}?page={page}", verbosity) for page in range(1, pages+1)]
        wait(scraping_futures)
        
        for completed in as_completed(scraping_futures):
            albums.update(completed.result())
    
    return albums


def download_videos(video, path):
    for vid in video:
        subprocess.call(
            ["/usr/bin/wget", "--tries", "0" , "--no-clobber", "--continue", "-q", "--show-progress", "-O", vid+".mp4", video[vid]["url"]]
        )


def fake_download(video, path):
    for vid in video:
        url = video[vid]["url"]
        print(f"Downloaded {url} to {path}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("url", type=str, help="Url of the Erome Playlist")
    parser.add_argument("-f", "--folder", help="Download path", default=Path.cwd(), type=Path)
    parser.add_argument("-a", "--profile", help="Download entire profile", action="store_true")
    parser.add_argument("-p", "--pretend", help="Fake download the videos", action="store_true")
    
    arguments = parser.parse_args()
    
    if arguments.folder.exists() and arguments.folder.is_dir():
        chdir(arguments.folder)
    else:
        print("Destination not found")
        exit(1)
    
    videos = {}
    download_fn = {"folder": arguments.folder}
    
    if arguments.pretend:
        download_fn["fn"] = fake_download
    else:
        download_fn["fn"] = download_videos
    
    if arguments.profile:
        videos = scrape_profile(arguments.url, download_fn)
    else:
        videos = scrape_album(arguments.url, arguments.url, download_fn)
        print(videos)
    
    if arguments.pretend:
        fake_download(videos, arguments.folder)
    else:
        download_videos(videos, arguments.folder)
