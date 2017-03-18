# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class SpankbangSpider(scrapy.Spider):
    name = "spankbang"
    allowed_domains = ["spankbang.com"]
    start_urls = ['http://spankbang.com/']

    def parse(self, response: HtmlResponse):
        next_link = response.css('link::href')
        print(next_link)
