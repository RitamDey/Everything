# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://dmoztools.net/Computers/Algorithms/"]
    start_urls = ['http://http://dmoztools.net/Computers/Algorithms//']

    def parse(self, response):
        pass
