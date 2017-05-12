# -*- coding: utf-8 -*-
import scrapy


class QuotesRandomSpider(scrapy.Spider):
    name = "quotes-random"
    allowed_domains = ["quotes.toscrape.com/random"]
    start_urls = ['http://quotes.toscrape.com/random/']

    def parse(self, response):

        quote_xpath = ""
        author_xpath = ""
        author_url_xpath = ""

        yield scrapy.Request(self.allowed_domains)
