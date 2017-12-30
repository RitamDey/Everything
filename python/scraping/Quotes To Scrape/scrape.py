from urllib import request
from lxml import html
import json


seen_urls = set(["http://quotes.toscrape.com",])
data = []


def parse(body):
    parser = html.parse(body)

    for quote_block in parser.xpath("//div[@class='quote']"):
        quote = quote_block.xpath("./span[@class='text']/text()")
        author = quote_block.xpath("./span[2]/small/text()") 
        data.append({
                        'quote': quote,
                        'author': author
                    })
    
    next_page = parser.xpath("//li[@class='next']/a/@href")
    if next_page:
        return request.urljoin(
                "http://quotes.toscrape.com",
                next_page[0]
            )
    else:
        return None


if __name__ == '__main__':
    next_url = parse(request.urlopen("http://quotes.toscrape.com"))
    print("Fetched http://quotes.toscrape.com")

    while next_url:
        if next_url in seen_urls:
            continue
        seen_urls.add(next_url)
        print("Parsed", next_url)
        next_url = parse(request.urlopen(next_url))
        print("Fetching", next_url)

    with open("data.json", "w+") as fout:
        json.dump(data, fout)

