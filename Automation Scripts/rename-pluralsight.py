import os
import shutil
from re import findall
from sys import argv, exit


if len(argv) < 2:
    print("Video directory not given")
    exit(1)


def move(direc):
    print(os.listdir(direc))
    for vid in os.listdir(direc):
        format = findall(r"\.\w{3}", vid)
        mod_chap = findall(r"mo?d?\d+\-?.*\-\d+", vid)
        if mod_chap:
            print(f"Moving {vid} -> {mod_chap}")
            shutil.move(direc+"/"+vid, direc+"/"+mod_chap[0]+format[0])

for direc in argv[1:]:
    move(direc)
