# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem


class BookspiderSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com', ]
    start_urls = ['http://books.toscrape.com/', ]

    def parse(self, response):
        # All the selectors used in this scraper
        book_selector = '//article[@class="product_pod"]'
        next_page_selector = '//div/ul[@class="pager"]/li[@class="next"]/a/@href'

        name_selector = './/h3/a/@title'
        image__selector = './/div[@class="image_container"]/a/img[@class="thumbnail"]/@src'
        book_link_selector = './/div[@class="image_container"]/a/@href'
        
        book = BookItem()
        fout = open('to-scarpe.txt', 'w+')
        
        # All the top-level extractions in this page
        products = response.xpath(book_selector)
        next_page = response.xpath(next_page_selector).extract_first()
        
        # The main loop for extraction of product information
        for product in products:
            book['name'] = product.xpath(name_selector).extract_first(),
            book['picture'] = response.urljoin(product.xpath(image__selector).extract_first())
            book['url'] = response.urljoin(product.xpath(book_link_selector).extract_first())
            print(book['url'], file=fout)
            yield book
        fout.close()

        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
                )
