from scrapy import Spider, Request
from MyScrapers.items import QuotesItem



class QuoteSpider(Spider):
    name = "quotes"
    allowed_domains = ['http://quotes.toscrape.com/*']
    start_urls = ['http://quotes.toscrape.com/',]

    # All the selectors 
    quotes_selector = '//div/div[@class="row"]/div[@class="col-md-8"]/div[@class="quote"]'
    quote_selector = './span[@class="text"]/text()'
    author_selector = './span[2]/small/text()'
    next_selector = '//nav/ul/li/a/@href'

    def parse(self, response):
        quotes = QuotesItem()

        for quote in response.xpath(self.quotes_selector):
            quotes['quote'] = quote.xpath(self.quote_selector).extract_first()[1:-1]
            quotes['author'] = quote.xpath(self.author_selector).extract_first()
            yield quotes
        
        next_page = response.xpath(self.next_selector).extract_first()

        if next_page is not None:
            yield Request(
                response.urljoin(next_page),
                callback=self.parse
            )