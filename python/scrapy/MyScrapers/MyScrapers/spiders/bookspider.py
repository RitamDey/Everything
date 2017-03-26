# -*- coding: utf-8 -*-
import scrapy

from ..items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com', ]
    start_urls = ['http://books.toscrape.com/', ]

    # All the selectors used in this scraper
    book_selector = '//article[@class="product_pod"]'
    next_page_selector = '//div/ul[@class="pager"]/li[@class="next"]/a/@href'

    name_selector = './/h3/a/@title'
    image_selector = './/div[@class="image_container"]/a/img[@class="thumbnail"]/@src'
    book_link_selector = './/div[@class="image_container"]/a/@href'

    def parse(self, response):
        book = BookItem()

        # All the top-level extractions in this page
        products = response.xpath(self.book_selector)
        next_page = response.xpath(self.next_page_selector).extract_first()
        
        # The main loop for extraction of product information
        for product in products:
            book['name'] = product.xpath(self.name_selector).extract_first(),
            book['image_urls'] = [
                f"http://books.toscrape.com{product.xpath(self.image_selector).extract_first()[2:]}", ]
            book['url'] = response.urljoin(product.xpath(self.book_link_selector).extract_first())
            # print(book['image_urls'])
            yield book

        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
