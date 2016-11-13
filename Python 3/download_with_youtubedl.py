import youtube_dl

urls = []
while True:
    try:
        urls.append(input())
    except EOFError:
        break

with youtube_dl.YoutubeDL({}) as obj:
    obj.download(urls)

