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
        title=''.join(tree.xpath('//h1[@class="title"]/text()')).strip()
        price=tree.xpath('//strong[@class="price-this"]//text()')[1]
        all_price=tree.xpath('//div[@class="summary-price-wrap"]/span[@class="quankuan"]/text()')[0]
        reg_date=tree.xpath('//div[@class="summary-attrs"]/dl[1]/dd/text()')[0]
        mile=tree.xpath('//div[@class="summary-attrs"]/dl[2]/dd/text()')[0]
        item['title']=title
        item['price']=price
        item['all_price']=all_price
        item['reg_date']=reg_date
        item['mile']=mile
        item['city_name']='none'
        item['detail_url']='none'
        item['displace']='none'
        item['source_id']='none'
        print(title)
        print(price)
        print(all_price)
        print(reg_date)
        print(mile)
        yield item
