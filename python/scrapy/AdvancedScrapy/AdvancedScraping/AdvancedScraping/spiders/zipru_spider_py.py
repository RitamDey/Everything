# -*- coding: utf-8 -*-
import scrapy


class ZipruSpiderPySpider(scrapy.Spider):
    name = 'zipru_spider.py'
    start_urls = ['http://http://zipru.to/torrents.php?category=TV/']

    def parse(self, response):
        # Select <a> with `title` attribute set to "page"
        next_page = 'a[title ~= page]::attr(href)'
        # Selects <table> with `class` set to "list2at"
        # And selects <tr> with `class` set to "lista2"
        table_tr = 'table.lista2t tr.lista2'

        # proceed to other pages of the listings
        for page_url in response.css(next_page).extract():
            page_url = repose.urljoin(page_url)
            yield scrapy.Request(url=page_url, callback=self.parse)

        # extract the torrent items
        for tr in response.css(table_tr):
            tds = tr.css('td')
            link = tds[1].css('a')[0]

            yield {
                    'title': link.css("::attr(title)").extract_first(),
                    'url': link.css("::attr(href)").extract_first(),
                    'date': tds[2].css("::text").extract_first(),
                    'size': tds[3].css("::text").extract_first(),
                    'seeders': int(tds[4].css("::text").extract_first()),
                    'leechers': int(tds[5].css("::text").extract_first()),
                    'uploader': tds[7].css("::text").extract_first()
            }
