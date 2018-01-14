# -*- coding: utf-8 -*-
from ..linkextractors import Extractor
from scrapy.spiders import CrawlSpider, Rule


class EromeSpider(CrawlSpider):
    name = 'EroMe'
    start_urls = ['https://www.erome.com/RealCamSluts',]

    rules = (
        Rule(
            Extractor(restrict_xpaths=("//ul[@class='pagination']/li[last()]/a")),
            callback='parse_item',
            follow=True
        ),  # last() gets the last <li>
    )

    def parse_item(self, response):
        i = {}
        videos = "//div[@class='container']/div[@id='albums']/div"
        video_id = "./@id"
        video_url = "./a/@href"
        video_title = "./a/div[@class='album-title']/text()"
        check_video_title = "indiansweety [f] - Camsgram.com/indiansweety"

        for video in response.xpath(videos):
            i['video_id'] = video.xpath(video_id).extract_first()
            i['url'] = video.xpath(video_url).extract_first()
            title = video.xpath(video_title).extract_first()
            if title in ["mirandacollins [f] - Camsgram.com/mirandacollins", "amy_on_fire [f] - Camsgram.com/amy_on_fire", "amirabelle4u [f] - Camsgram.com/amirabelle4u", "eileen_rose [f] - Camsgram.com/eileen_rose"]:
                yield i

