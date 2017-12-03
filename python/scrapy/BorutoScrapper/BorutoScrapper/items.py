# -*- coding: utf-8 -*-
from scrapy import Item, Field


class BorutoscrapperItem(Item):
    # define the fields for your item here like:
    folder_path = Field()
    image_urls = Field()
    source_url = Field()
