from bs4 import BeautifulSoup


infile = open("example.xml", "r")
contents = infile.read()
soup = BeautifulSoup(contents, 'xml')

titles = soup.find_all('title')
authors = soup.find_all('author')
prices = soup.find_all('price')

for item in zip(titles, authors, prices):
    print("{0} by {1} costs {2}".format(
        item[0].get_text(),
        item[1].get_text(),
        item[2].get_text()
        ))

