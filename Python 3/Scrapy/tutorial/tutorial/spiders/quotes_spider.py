import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://quotes.toscrape.com/page/1',
            'http://quotes.toscrape.com/page/2',
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
                text = str(quote.css('span.text::text').extract_first())[1:-1],
                author =  quote.css('span small::text').extract_first(),
                # 'tags': quote.css('div.tags a.tag::text').extract(),

                yield {
                    'quote': f'{text[0]} \n by {author[0]}',
                }
