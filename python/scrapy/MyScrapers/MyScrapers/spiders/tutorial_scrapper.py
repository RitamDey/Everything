# -*- coding: utf-8 -*-
from scrapy import Spider


class TutorialScrapperSpider(Spider):
    name = 'tutorial-scrapper'
    # allowed_domains not needed
    start_urls = ['https://www.digitalocean.com/community/api/tutorials/search?facets=*&page=1&q=&primary_filter=newest&per_page=21']

    def parse(self, response):
        print(response.body)
