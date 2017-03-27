# -*- coding: utf-8 -*-
import scrapy


class PythonDownloaderSpider(scrapy.Spider):
    name = "python_downloader"
    allowed_domains = ["www.python.org"]
    start_urls = ['http://www.python.org/downloads']

    def parse(self, response):
        # Selectors

        # This selector selects the block where the main download buttons are located
        main_block_selector = '//div[@id="touchnav-wrapper"]\
                                /header[@class="main-header"]\
                                /div[@class="container"]\
                                /div[2]'

        # This selector selects the latest Python3 download url
        download_selector = './div/div[2]/p/a/@href'

        main_block = response.xpath(main_block_selector)
        download_url = main_block.xpath(download_selector).extract_first()

        print(download_url)