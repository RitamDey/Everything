import glob
import re
import os


os.chdir("/media/stux/WD Backup/Videos")

for folder in glob.glob("*S*"):
    season = re.findall(r"\d{2}", folder)
    renamed = "Season " + season[0]
    print(f"Renaming {folder} -> {renamed}")
    print(os.rename(folder, renamed))

print("Done")
