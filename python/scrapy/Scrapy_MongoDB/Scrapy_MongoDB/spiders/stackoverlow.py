# -*- coding: utf-8 -*-
import scrapy
from Scrapy_MongoDB.items import ScrapyMongodbItem


class StackoverlowSpider(scrapy.Spider):
    name = 'stackoverlow'
    start_urls = ['https://stackoverflow.com/questions?pagesize=50&sort=newest/']

    def parse(self, response):
        questions_xpath = "//div[@class='summary']"
        question_xpath = "./h3/a[@class='question-hyperlink']/text()"
        question_link = "./h3/a[@class='question-hyperlink']/@href"
        next_link = "//div[@class='pager fl']/a[@rel='next']/@href"

        for q in response.xpath(questions_xpath):
            item = ScrapyMongodbItem()
            item['name'] = q.xpath(question_xpath).extract_first()
            item['url'] = response.urljoin(q.xpath(question_link).extract_first())

            yield item

        yield scrapy.Request(response.urljoin(response.xpath(next_link).extract_first()),
                             callback=self.parse)
