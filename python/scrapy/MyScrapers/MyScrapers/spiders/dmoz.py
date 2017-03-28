# -*- coding: utf-8 -*-
from json import loads
from json.decoder import JSONDecodeError
import scrapy
from scrapy.log import INFO
from ..items import DomainItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["http://dmoztools.net/"]

    def start_requests(self):
        try:
            urls = loads(open('out.json', 'r').read())
            urls = [url['url'] for url in urls]
        except (FileNotFoundError, JSONDecodeError):
            urls = open('urls.txt', 'r')
            urls = [url for url in urls.read().split('\n')]

        for url in urls:
            # self.logger.log(INFO, url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # All the top-level selectors
        NEXT_PAGE_SELECTOR = ''
        PAGE_XPATH_SELECTOR = '//div[@id="site-list-content"][@class="results browse-content"]'
        PAGE_CSS_SELECTOR = 'div.site-item'

        # All the selectors for the domains
        PAGE_TITLE_SELECTOR = './/div[3]/a/div/text()'
        PAGE_DESCR_SELECTOR = './/div[3]/div/text()'
        PAGE_URL_SELECTOR = './/div[@class="title-and-desc"]/a/@href'

        domain = DomainItem()
        # Main loop to extract sites names
        for site in response.xpath(PAGE_XPATH_SELECTOR).css(PAGE_CSS_SELECTOR):
            domain['name'] = site.xpath(PAGE_TITLE_SELECTOR).extract_first()
            domain['desc'] = site.xpath(PAGE_DESCR_SELECTOR).extract_first()
            domain['desc'] = domain['desc'].replace('\r\n\t\t\t\r\n', '').strip()
            domain['url'] = site.xpath(PAGE_URL_SELECTOR).extract_first()
            yield domain


class DmozIndexSpider(scrapy.Spider):
    name = 'dmoz_index'
    allowed_domains = ["http://dmoztools.net/Computers/", ]
    start_urls = ['http://dmoztools.net/Computers/', ]
    # start_urls = ['http://dmoztools.net/']

    # ALl the selectors
    section_css_selector = 'div.content'
    section_xpath_selector = './div/section[2]/div'
    sub_section_selector = 'section.children'
    category_selecctor = './div/div'
    topic_selector = './a/div'
    topic_url_selector = './a/@href'

    def parse(self, response):
        sections = response.css(self.section_css_selector).xpath(self.section_xpath_selector)[0]

        urls = open('urls.txt', 'w+')

        for section in sections.css(self.sub_section_selector):
            for category in section.xpath(self.category_selecctor):
                url = response.urljoin(category.xpath(self.topic_url_selector).extract_first())
                yield {
                    'topic': category.xpath(self.topic_selector).extract()[0].split('\r\n')[2].strip(),
                    'url': url
                }
                print(url, file=urls)
