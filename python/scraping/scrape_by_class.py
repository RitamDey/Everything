from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html.read(), "lxml")
names = bs.findAll("span", {'class': 'green'}) # Find all <span> with green css class

for name in names:
    print(name.get_text())

