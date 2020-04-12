# TheSubDB Python SDK
# Copyright (C) 2020  Ritam Dey
import requests
from hashlib import md5
from os import path
import os


class SubtitleNotFound(Exception):
    pass


class SubtitleAlreadyExists(Exception):
    pass


class TheSubDB:
    _URL = "http://api.thesubdb.com"
    _parameters = {}

    def __init__(self, user_agent: str, file_name: str = None):
        if file_name:
            self.getHash(file_name)
        self._headers = {"User-Agent": user_agent}
        self._languages = None

    @classmethod
    def getSubtitleName(cls, file_name: str) -> str:
        """
        Process the given file name and creates the subtitle filename from that string
        """
        file_name = file_name.split(".")
        file_name[-1] = "srt"

        return ".".join(file_name)

    def getHash(self, file_name: str):
        """
        Calculates the hashcode for the file. Taken from http://thesubdb.com/api/
        """
        readsize = 64 * 1024
        with open(file_name, 'rb') as video_file:
            size = path.getsize(file_name)
            data = video_file.read(readsize)
            video_file.seek(-readsize, os.SEEK_END)
            data += video_file.read(readsize)

        video_hash = md5(data).hexdigest()
        self._parameters = {"hash": video_hash}

    def search(self, get_versions: bool = False):
        """
        Set-up the parameters and issue a search API call for the calculated hash
        """
        self._parameters["action"] = "search"
        if get_versions:
            self._parameters["versions"] = ""
        response = requests.get(
            self._URL, params=self._parameters, headers=self._headers)

        if response.status_code != 200:
            if response.status_code == 404:
                raise SubtitleNotFound()
            else:
                raise response.raise_for_status()

        self._clean_headers()
        return response.text

    def download(self, language: str, outfile: str):
        """
        Set-up the parameters and issue a download API call for the calculated hash.
        After the complete data is recieved, write it to the subtitle file
        """
        self._parameters["action"] = "download"
        self._parameters["language"] = language

        response = requests.get(
            self._URL, params=self._parameters, headers=self._headers)

        if response.status_code != 200:
            raise response.raise_for_status()

        with open(outfile, "w", encoding=response.encoding) as subtitle:
            subtitle.write(response.text)

        self._clean_headers()

    def upload(self, subtitle_file: str, video: str):
        self._parameters["action"] = "upload"
        with open(subtitle_file, "r") as subtitle_data:
            request_data = {
                "file": (subtitle_file, subtitle_data.read()),
                "hash": self.getHash(video)
            }

            response = requests.post(
                self._URL, params=self._parameters, headers=self._headers, files=request_data)

        if response.status_code == 403:
            raise SubtitleAlreadyExists()
        elif response.status_code == 415:
            raise TypeError("Unsupported Media Type")
        elif response.status_code == 400:
            raise response.raise_for_status()

    def _clean_headers(self):
        if "versions" in self._parameters:
            del self._parameters["versions"]
        if "language" in self._parameters:
            del self._parameters["language"]
        if "action" in self._parameters:
            del self._parameters["action"]


class SandboxAPI(TheSubDB):
    _URL = "http://sandbox.thesubdb.com"
