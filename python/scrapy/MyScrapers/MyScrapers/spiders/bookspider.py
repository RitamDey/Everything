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
        # All the selectors used in this scraper
        BOOK_SELECTOR = '//article[@class="product_pod"]'
        NEXT_PAGE_SELECTOR = '//div/ul[@class="pager"]/li[@class="next"]/a/@href'

        NAME_SELECTOR = './/h3/a/@title'
        IMAGE_SELECTOR = './/div[@class="image_container"]/a/img[@class="thumbnail"]/@src'
        BOOK_LINK_SELECTOR = './/div[@class="image_container"]/a/@href'
        
        book = BookItem()
        fout = open('to-scarpe.txt', 'w+')
        
        # All the top-level extractions in this page
        products = response.xpath(BOOK_SELECTOR)
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        
        # The main loop for extraction of product information
        for product in products:
            book['name'] = product.xpath(NAME_SELECTOR).extract_first(),
            book['picture'] = response.urljoin(product.xpath(IMAGE_SELECTOR).extract_first())
            book['url'] = response.urljoin(product.xpath(BOOK_LINK_SELECTOR).extract_first())
            print(book['url'], file=fout)
            yield book
        fout.close()
        
        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )
