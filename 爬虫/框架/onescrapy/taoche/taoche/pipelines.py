# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TaochePipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('10.10.21.151',27017)
        self.db=self.client['123']
        self.collection=self.db['car']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
