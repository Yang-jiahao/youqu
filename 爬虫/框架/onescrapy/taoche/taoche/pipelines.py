# -*- coding: utf-8 -*-
import pymongo
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TaochePipeline(object):
    def __init__(self):
        self.client=pymongo.MongoClient('localhost',27017)
        self.db=self.client['fenbupc']
        self.collection=self.db['fenbu']
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
