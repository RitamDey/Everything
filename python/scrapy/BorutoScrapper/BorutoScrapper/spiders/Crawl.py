# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BorutoscrapperItem


class CrawlSpider(CrawlSpider):
    name = 'Crawl'
    allowed_domains = ['www.mangapanda.com']
    start_urls = ['http://www.mangapanda.com/boruto/1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='navi']/div[@class='prevnext']/span[@class='next']/a")), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        image = BorutoscrapperItem()
        image['image_urls'] = response.xpath('//div[@id="imgholder"]/a/img/@src').extract()
        image['folder_path'] = image['image_urls'][0].split("/")[-2]
        return image
