# -*- coding: utf-8 -*-
import scrapy
from r_earthporn.items import ImageItem


class PostsSpider(scrapy.Spider):
    name = 'Posts'
    start_urls = ['https://www.reddit.com/r/EarthPorn/']

    def parse(self, response):
        table_xpath = "//div[@id='siteTable']/div"
        href_xpath = "./a/@href"
        title_xpath = "./div[2]/div[@class='top-matter']/p[@class='title']/a/text()"

        images = ImageItem()
        links = response.xpath(table_xpath).xpath(href_xpath)
        titles = response.xpath(table_xpath).xpath(title_xpath)

        for title, link in zip(titles,links):
            images["name"] =  title.extract(),
            images["link"] = link.extract()

            yield images

