from sys import argv
import youtube_dl

with youtube_dl.YoutubeDL({}) as obj:
    obj.download(argv[1:])

