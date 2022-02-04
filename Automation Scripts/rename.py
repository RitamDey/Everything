#!/usr/bin/env python3
import re
import pathlib
import argparse


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("path", help="media path", type=pathlib.Path)
arguments = argument_parser.parse_args()
path = arguments.path.expanduser()
regex = re.compile(r"E\d+")

for files in path.iterdir():
    file_name = files.stem
    episode = re.search(regex, file_name)
    if episode is None: continue
    new_name = files.with_stem(episode.group())
    print(f"{files.name} => {new_name.name}")
    files.rename(new_name)

