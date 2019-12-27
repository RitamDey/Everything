import requests
from sys import argv, exit
from subprocess import call


headers = {'x-reddaid': 'Z223NAN3ZHMJ63AA',
 'x-reddit-loid': '00000000000011p51y.2.1474968482720.Z0FBQUFBQmQ0azZsZkxPaExuZndEYWktMkw3M2lNRUh3cXpaQlU0aEJjVmR0U3hwdjBDREthV1hwMmMtU21MSDV3NzM4RjN3NDRXaUtZTjFTNVM2VnZYbmZGUXdPNm1IYlp4OGVnV0R4NkduejZSOEZDbFMyM2hKN0p6OVFWUUV5cTVwdUEyaW1iZzA',
 'x-reddit-session': 'Zru5BNaZKHQItPwKDK.0.1577008705172.Z0FBQUFBQmRfejVCc1RkYmd5RldOcm02OGVoVTZRZ3d2WjNJTVJMaGJpX3lTSm44c2thRlFIYnFzZmFwck5Iam45T1BBTm9PaFo4bWM4Z2lZSmhuVHhFNENnd0FfZDBXanYzOTM3Z2tfV0dqTi1qWTZ0eHJYQ0d2MEdjR09fUkJsd0xmYnBMQnk4Z08',
 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

params = {'rtj': 'only',
'redditWebClient': 'web2x',
'app': 'web2x-client-production',
'allow_over18': '1',
'include': 'identity,structuredStyles,prefsSubreddit',
'after': '',
'dist': '25',
'layout': 'card',
'sort': 'new',
'geo_filter': 'IN'}


def download(post_count=25):
    iter_counts = post_count // 25

    for _ in range(iter_counts):
        response = requests.get("https://gateway.reddit.com/desktopapi/v1/subreddits/EarthPorn+ExposurePorn+ImaginaryLandscapes+ImaginaryTechnology+SkyPorn+wallpapers", headers=headers, params=params)

        if response.status_code != 200:
            continue

        last_seen = None
        posts = response.json()["posts"]
        for post in posts:
            last_seen = post
            title = posts[post]["title"]
            url = posts[post]["media"]["content"]

            print(f"{title} => {url}")
            call(["/usr/bin/wget", "-q", "--show-progress", "-O", title, url])


if __name__ == '__main__':
    if len(argv) < 2:
        print("Give a download count")
        exit(1)

    download(post_count=int(argv[1]))

