import requests
from hashlib import md5
from os import path, chdir, listdir, getcwd
from sys import argv
from thesubdb import TheSubDB
from glob import glob

API = TheSubDB("SubDB/1.0 (Pyrrot/0.1; http://github.com/jrhames/pyrrot-cli")

def crawl_folder(folder):
    """
    Crawls the sub-directory structure and downloads subtitles when found
    """
    print(f"Crawling for videos in folder {folder}")
    chdir(folder)
    
    for e in listdir(getcwd()):
        if path.isdir(e):
            crawl_folder(e)
            chdir("..")
        elif path.isfile(e) and (e.endswith("mkv") or e.endswith("mp4")):
            download_subtitle(e)


def download_subtitle(video_name: str):
    print(f"Downloading subtitles for video {video_name}", end=" ")
    srt_name = TheSubDB.getSubtitleName(video_name)
    if path.exists(srt_name) and path.isfile(srt_name):
        print(f"Subtitle {srt_name} already exists. Skipping...")
    API.getHash(video_name)
    languages = API.search().split(",")
    if "en" not in languages:
        print(f"English subtitles not avaliable for {video_name}")
        return
    try:
        API.download(language="en", outfile=srt_name)
    except requests.exceptions.HTTPError:
        print("Skipping download due to error.")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please specify a folder containing videos or other subfolders")
        exit(1)

    for video_folder in argv[1:]:
        if path.exists(video_folder):
            print(f"Downloading for {video_folder}")
            if path.isdir(video_folder): crawl_folder(video_folder)
            elif path.isfile(video_folder): download_subtitle(video_folder)
        else:
            print(f"Unknown directory: {video_folder}")
