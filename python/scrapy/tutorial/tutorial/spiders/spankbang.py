# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.response.html import HtmlResponse


class SpankbangSpider(scrapy.Spider):
    name = "spankbang"
    allowed_domains = ["spankbang.com"]
    start_urls = ['http://spankbang.com/']

    def parse(self, response: HtmlResponse):
        fout = open('crawl.txt', 'w')
        video_url = response.css('a.thumb').xpath('@href').extract()
        video_name = response.css('img.cover').xpath('@alt').extract()
        for vid_name, vid_url in zip(video_name, video_url):
            print(f"Video {vid_name}: https://www.spankbang.com{vid_url}", sep='\n', file=fout)
        fout.close()
