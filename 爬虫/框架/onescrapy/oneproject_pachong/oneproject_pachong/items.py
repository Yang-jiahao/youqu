# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# 这个就是Django中的module

class OneprojectPachongItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义字段
    # 这是定义一个文档，然后对文档进行存储,因为这是字典样式
    rank = scrapy.Field()
    title = scrapy.Field()
    state = scrapy.Field()
    types = scrapy.Field()
    tv = scrapy.Field()
    uptime = scrapy.Field()
    # 将数据封装到一个字典文档中，便于向mongoDB保存

