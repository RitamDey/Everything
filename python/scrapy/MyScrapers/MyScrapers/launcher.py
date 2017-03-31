from scrapy.spider import Spider
from spiders.dmoz import DmozSpider, DmozIndexSpider
from twisted.internet import reactor
from scrapy import log
from scrapy.settings import Settings
from scrapy.settings import CrawlerSettings

def spider_closed(spider: Spider):
    if spider.name == 'dmoz_index':
        urls = open('urls.txt', 'r').read().split('\n')
        crawler = Crawler(DmozSpider)


settings = Settings()
crawler = CrawlerSettings(settings)
crawler
