import glob
import re
import os
from os import path


def rename():
    for folder in os.listdir():
        for files in glob.glob(folder + "/" + "*.mkv"):
            name = folder + "/" + re.findall(r'E\d{2}', files)[0] + ".mkv"
            print(f"{files} -> {name}")
            os.rename(files, name)


rename()
