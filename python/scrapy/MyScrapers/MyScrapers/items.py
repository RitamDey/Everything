# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BookItem(Item):
    name = Field()
    desc = Field()
    url = Field()
    images = Field()  # Needed to hold images
    image_urls = Field()  # Needed to hold image_urls


class DomainItem(Item):
    name = Field()
    desc = Field()
    url = Field()


class QuotesItem(Item):
    quote = Field()
    author = Field()
    url = Field()
