# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SteamSpider(CrawlSpider):
    name = 'steam'
    #allowed_domains = ['https://store.steampowered.com/']
    start_urls = ['https://store.steampowered.com/search/?sort_by=Released_DESC/']

    rules = (
        Rule(
            LinkExtractor(
                restrict_css=[".search_result_row",]
            ),
            callback='parse_item',
            follow=True
        ),

        #Rule(
        #    LinkExtractor(
        #        restrict_css=[".search_pagination_right",]
        #        restrict_xpath=["./a[@class='pagebtn'][last()]",]
        #    ),
        #    follow=True
        #)
    )

    def parse_item(self, response):
        i = {}

        i['title'] = response.css(".details_block").xpath("./text()")[1].extract()
        return i
