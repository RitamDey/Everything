""""
This scrapper is used to scrape the DigitalOcean's vast tutorials for a particular topic
"""

import scrapy


class DigitalScrapper(scrapy.Spider):
    name = "DigitalScrapper"
    start_urls = ['https://www.digitalocean.com/community/tutorials', ]


    def parse(self, response):

        MAIN_BLOCK_SELECTOR = 'div.feedable-details'

        for blocks in response.css(MAIN_BLOCK_SELECTOR):
            LINK_SELECTOR = './/h3/a/@href'
            TITLE_SELECTOR = './/h3/a/text()'

            for link, title in zip(blocks.xpath(LINK_SELECTOR), blocks.xpath(TITLE_SELECTOR)):
                yield {
                        'title': title.extract(),
                        'link': response.urljoin(link.extract())
                }

                # TODO: Implement threading to go and crawl every page in the tutorials
