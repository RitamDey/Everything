# -*- coding: utf-8 -*-
import scrapy


class SpankbangSpider(scrapy.Spider):
    name = "spankbang"
    allowed_domains = ["spankbang.com"]
    start_urls = ['http://spankbang.com/']

    def parse(self, response):
        pass
