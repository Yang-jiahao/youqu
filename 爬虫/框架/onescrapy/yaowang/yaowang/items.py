# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YaowangItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    store = scrapy.Field()
    urlx = scrapy.Field()


    brand = scrapy.Field()#品牌
    sizes = scrapy.Field()#规格
    weights = scrapy.Field()#重量
    manufacturer = scrapy.Field()#生产商家
    approval_number = scrapy.Field()#批准号


class YouxinItem(scrapy.Item):
    # define the fields for your item here like:
    '''
    标题，价格，公里数，仓库，年限，图片，认证，首付信息
    '''
    title = scrapy.Field()
    price = scrapy.Field()
    gongli = scrapy.Field()
    cangku = scrapy.Field()
    age = scrapy.Field()
    img = scrapy.Field()
    renzheng = scrapy.Field()
    shoufu = scrapy.Field()

class TongjijuItem(scrapy.Item):
    pass