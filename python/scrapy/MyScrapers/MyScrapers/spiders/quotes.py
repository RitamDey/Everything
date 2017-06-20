# -*- coding: utf-8 -*-
from scrapy import Spider, Request

from ..items import QuotesItem


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes_selector = '//div[@class="container"]/div[@class="row"]/div[@class="col-md-8"]/div[@class="quote"]'
        quote_selector = './span[@class="text"]/text()'
        author_selector = './span[2]/small[@class="author"]/text()'
        # author_url_selector = './span[2]/a/@href'
        tags = './div[@class="tags"]/a[@class="tag"]'

        quote_item = QuotesItem()

        for quote in response.xpath(quotes_selector):
            quote_item['quote'] = quote.xpath(quote_selector).extract_first()[1:-1]
            quote_item['author'] = quote.xpath(author_selector).extract_first()

            quote_item['tags'] = [
                tag.xpath('./text()').extract_first().capitalize() \
                for tag in quote.xpath(tags)
                ]

            yield quote_item

        next_link = '//div[@class="container"]/div[@class="row"]/div[@class="col-md-8"]/nav/ul[' \
                    '@class="pager"]/li[@class="next"]/a/@href '

        yield Request(
            response.urljoin(response.xpath(next_link).extract_first()),
            callback=self.parse
        )
