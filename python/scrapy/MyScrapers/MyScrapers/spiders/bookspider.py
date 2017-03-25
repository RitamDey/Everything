# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com',]
    start_urls = ['http://books.toscrape.com/',]

    # rules = (
    #     Rule(LinkExtractor(allow=r'div'), callback='parse_item', follow=True),
    # )

    # def parse_item(self, response):
    def parse(self, response):
        book = BookItem()
        BOOK_NAME_SELECTOR = ''

        NEXT_PAGE_SELECTOR = '//div/ul[@class="pager"]/li[@class="next"]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        return scrapy.Request(response.urljoin(next_page))
