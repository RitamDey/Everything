import urllib.request
import sys
from bs4 import BeautifulSoup as bs


def req(url):
    global res
    res = urllib.request.urlopen(url=url)


def scrap():
    global res
    obj = bs(res.read(), "html.parser")
    return obj.title


def main():
    for arg in sys.argv[1:]:
        req('http://' + arg)
        title = scrap()
        print(arg + " : " + title)


if __name__ == '__main__':
    main()
