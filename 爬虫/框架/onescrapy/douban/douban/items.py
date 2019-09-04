# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    xiaourl = scrapy.Field()
    b_name = scrapy.Field()
    score = scrapy.Field()

    author = scrapy.Field()
    publisher = scrapy.Field()
    gu_fast = scrapy.Field()
    translator = scrapy.Field()
    publication = scrapy.Field()
    page = scrapy.Field()
    price = scrapy.Field()
    paperback = scrapy.Field()
    collection = scrapy.Field()


