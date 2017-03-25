# -*- coding: utf-8 -*-
import scrapy.spider import BaseSider
from newcoder.items import NewcoderItem


class LivingsocialSpider(BaseSpider):
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ['http://livingsocial.com/']

    deals_list_xpath = '//li[@dealid]'
    item_field = {
        'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
        'link': './/a/@href',
        'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
        'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
        'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
        'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
    }


