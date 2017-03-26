# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
    images = scrapy.Field()  # Needed to hold images
    image_urls = scrapy.Field()  # Needed to hold image_urls


class DomainItem(scrapy.Item):
    name = scrapy.Field()
    desc = scrapy.Field()
    url = scrapy.Field()
