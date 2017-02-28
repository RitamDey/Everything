from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html") # Get the html doc

bsObj = BeautifulSoup(html.read(), 'lxml') # Create bs4 object with lxml parser and let it parse the html doc
print(bsObj.h1) # print whats in <h1>

