# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class ScrapyMongodbPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
                "mongodb://ritam_dey:ThisIsPassword@scrapyexample-shard-00-00-thkmu.mongodb.net:27017,scrapyexample-shard-00-01-thkmu.mongodb.net:27017,scrapyexample-shard-00-02-thkmu.mongodb.net:27017/test?ssl=true&replicaSet=ScrapyExample-shard-0&authSource=admin")

        db = connection["stackoverflow"]
        self.collection = db["data"]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added", level=log.DEBUG, spider=spider)

        return item
