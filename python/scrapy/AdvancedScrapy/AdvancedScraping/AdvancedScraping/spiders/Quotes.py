# -*- coding: utf-8 -*-
import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'Quotes'
    start_urls = ['http://www.goodreads.com/quotes/tag/atheism/']

    def parse(self, response):
        item = QuoteItem()
        quote_block_xpath = "//div[@class='quoteDetails ']"
        quote_xpath = "./div[@class='quoteText']/text()"
        author_xpath = "./div[@class='quoteText']/a/text()"
        tags = "./div[@class='quoteFooter']/div[@class='greyText smallText left']/a/text()"

        for block in response.xpath(quote_block_xpath):
            item['quote'] = block.xpath(quote_xpath).extract_first().strip()
            item['author'] = block.xpath(author_xpath).extract_first()
            item['tags'] = block.xpath(tags).extract()
            yield item
        
        next_page = response.xpath("//a[@class='next_page'][@rel='next']/@href").extract_first()
        yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

