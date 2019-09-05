# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import TaocheItem
from .city import CITY_CODE
from .city import CAR_CODE_LIST
from scrapy_redis.spiders import RedisSpider

city_list=CITY_CODE
pai=CAR_CODE_LIST

class TaocheyaSpider(RedisSpider):
    name = 'taocheya'
    redis_key = 'taoche:start_urls'
    # allowed_domains = ['taoche.com']
    # start_urls = []
    # for i in city_list:
    #     url=f'https://{i}.taoche.com/all/'
    #     start_urls.append(url)

    def parse(self, response):
        html = response.body.decode("utf-8")
        tree = etree.HTML(html)
        urlx_list = tree.xpath('//a[@class="title"]/@href')#详情页
        if urlx_list is None:
            pass
        else:
            print(urlx_list)
            for x in urlx_list:
                url='https:'+x
                yield scrapy.Request(url=url,callback=self.parse_detil)
            print('='*100)
    def parse_detil(self,response):
        item = TaocheItem()
        tree=etree.HTML(response.body.decode('utf-8'))
        title=tree.xpath('//h1[@class="title"]/text()')
        price=tree.xpath('//strong[@class="price-this"/span[position()=1]//text()')
        all_price=tree.xpath('//strong[@class="price-this"]/span[position()=2]/text()')
        reg_date=tree.xpath('//div[@class="summary-attrs"]/dl[position()=1]/dd/text()')
        mile=tree.xpath('//div[@class="summary-attrs"]/dl[position()=2]/dd/text()')
        item['title']=title
        item['price']=price
        item['all_price']=all_price
        item['reg_date']=reg_date
        item['mile']=mile
        print(title)
        print(price)
        print(all_price)
        print(reg_date)
        print(mile)
        yield item
