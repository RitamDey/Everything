# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from r_earthporn.items import ImageItem


class PostsSpider(scrapy.Spider):
    name = 'Posts'
    start_urls = ['https://www.reddit.com/r/EarthPorn/']

    def parse(self, response):
        table_xpath = "//div[@id='siteTable']/div"
        href_xpath = "./a/@href"
        title_xpath = "./div[2]/div[@class='top-matter']/p[@class='title']/a/text()"

        links = response.xpath(table_xpath).xpath(href_xpath)

        for link in links:
            link = link.extract()
            if link.find("/r/") != -1:
                yield Request(url=response.urljoin(link), callback=self.parse_post)


    def parse_post(self, response):
        title_xpath = "//div[@class='top-matter']/p[@class='title']/a/text()"
        picture_xpath = "//div[@class='media-preview-content']/a/@href"

        picture = response.xpath(picture_xpath).extract_first()
        title = response.xpath(title_xpath).extract_first()

        yield {
                "title": title,
                "picture": picture
        }
