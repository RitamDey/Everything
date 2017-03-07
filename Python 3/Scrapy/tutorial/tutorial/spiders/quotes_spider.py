import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
                text = str(quote.css('span.text::text').extract_first())[1:-1],
                author =  quote.css('span small::text').extract_first(),
                yield {
                    'quote': f'{text[0]} \n by {author[0]}',
                }

                nxt = response.css('li.next a::attr(href)').extract_first()
                if nxt is not None:
                    nxt = response.urljoin(nxt)
                    yield scrapy.Request(nxt, callback=self.parse)
