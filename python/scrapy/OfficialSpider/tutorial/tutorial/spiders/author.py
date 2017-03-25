# -*- coding: utf-8 -*-
import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author+a::attr(href)').extract_first():
                yield scrapy.Request(reponse.urljoin(href), callback=self.parse_author)
        
