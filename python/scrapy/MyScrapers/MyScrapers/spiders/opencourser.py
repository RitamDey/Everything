# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class CourseExtractor():

    def extract_links(self, response):
        course_selector = ''
        pass


class OpencourserSpider(CrawlSpider):
    name = 'opencourser'
    allowed_domains = ['http://opencourser.com/']
    start_urls = ['http://http://opencourser.com/browse/?category=48/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(CourseExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        pass
