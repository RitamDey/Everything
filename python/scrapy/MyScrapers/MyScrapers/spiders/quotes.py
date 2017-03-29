# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import QuotesItem


class QuotesSpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=r'^page/\d*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        quotes_selector = '//div[@class="row"]/div[@class="col-md-8"]/div[@class="quote"]'
        quote_selector = './span[@class="text"]'
        author_selector = './span[2]/small[@class="author"]'
        author_url_selector = './span[2]/a'

        quote_item = QuotesItem()

        for quote in quotes_selector:
            quotes_selector['quote'] = quote.xpath(quote_selector).extract_first()[1:-1]
            quotes_selector['author'] = quote.xpath(author_selector).extract_first()
            quotes_selector['author_url'] = quote.xpath(author_url_selector).extract_first()

            yield quote_item
