# -*- coding: utf-8 -*-
import scrapy
from json import loads
from MyScrapers.items import QuotesItem as Quotes

class ScrollingQuotesSpider(scrapy.Spider):
    name = 'scrolling-quotes'
    # allowed_domains attribute causes trouble
    start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']
    base_url = 'http://quotes.toscrape.com/api/quotes?page='

    def parse(self, response):
        res = loads(response.body)

        for quote in res['quotes']:
            yield Quotes({
                        'quote': quote['text'],
                        'author': quote['author']['name'],
                        'tags': quote['tags']
                })

        if res['has_next']:
            yield scrapy.Request(
                    "{0}{1}".format(self.base_url, res['page']+1),
                    callback=self.parse
                )
