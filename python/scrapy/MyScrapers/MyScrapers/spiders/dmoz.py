# -*- coding: utf-8 -*-
import scrapy


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://dmoztools.net/Computers/Algorithms/"]
    start_urls = ['http://http://dmoztools.net/Computers/Algorithms//']

    def parse(self, response):

        # All the top-level selectors
        NEXT_PAGE_SELECTOR = ''
        PAGE_SELECTOR = ''

        # All the selectors for the domains
        PAGE_NAME_SELECTOR = ''
        PAGE_URL_SELECTOR = ''

        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()

        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callable=self.parse
            )
