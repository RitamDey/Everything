# -*- coding: utf-8 -*-
import scrapy


class DummySpiderSpider(scrapy.Spider):
    name = 'dummy_spider'
    allowed_domains = ['zipru.to/torrents.php?category=TV']
    start_urls = ['http://zipru.to/torrents.php?category=TV/']

    def parse(self, response):
        # The css selector is same as //a[@title='page']/@href 
        # which can also be written as //a[contains(@title, "page ")]/@href
        for page_url in response.css('a[title ~= page]::attr(href)').extract():
            page_url = response.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)

        for tr in response.css('table.lista2t tr.lista2'):
            tds = tr.css('td')
            link = tds[1].css('a')[0]
            yield {
                'title': link.css('::attr(title)').extract_first(),
                'url' : response.urljoin(link.css('::attr(href)').extract_first()),
                'date' : tds[2].css('::text').extract_first(),
                'size' : tds[3].css('::text').extract_first(),
                'seeders': int(tds[4].css('::text').extract_first()),
                'leechers': int(tds[5].css('::text').extract_first()),
                'uploader': tds[7].css('::text').extract_first(),
            }

