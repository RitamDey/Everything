# -*- coding: utf-8 -*-
import scrapy


class IndexSpider(scrapy.Spider):
    name = 'Index'
    allowed_domains = ['www.mangapanda.com/boruto']
    start_urls = ['http://www.mangapanda.com/boruto']

    def parse(self, response):
        data_xpath = "//table[@id='listing']/tr/td/a/@href"

        with open("links.txt", "w+") as fout:
            for link in response.xpath(data_xpath):
                to_write = self.start_urls[0]+link.extract()
                print(to_write, file=fout)
