# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from lxml import etree
from ..items import YouxinItem

class YouxinSpider(scrapy.Spider):
    name = 'youxin'
    allowed_domains = ['xin.com']
    start_urls = []
    city_list = open('E:\爬虫\框架\onescrapy\yaowang\yaowang\ershouche.json','r', encoding='utf-8')
    citys = city_list.read()
    citys_dic=json.loads(citys)
    emlist=citys_dic['data']['city_all']
    for k,v in emlist.items():
        ename=v['ename']
        for i in range(1,2):
            url=f'https://www.xin.com/{ename}/i{i}/?channel=a49b117c44837d110753e751863f53'
            start_urls.append(url)
    def parse(self, response):
        print('============================================================================')
        res = response.body.decode('utf-8')
        tree = etree.HTML(res)
        li_list=tree.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        for li in li_list:
            che=YouxinItem()
            print('123321')
            title = li.xpath('//h2/span/text()')[0]
            price = li.xpath('//div[@class="across"]//em/text()')[0].strip()
            gongli = li.xpath('//div[@class="pad"]/span//text()')[2:4]
            cangku = li.xpath('//div[@class="pad"]/span/span/text()')
            age = li.xpath('//div[@class="pad"]//span/text()[1]')
            img = li.xpath('//img/@data-original')
            renzheng = li.xpath('//span[@class="caritem-icon yxrz-icon"]//text()[last()]')
            shoufu = li.xpath('//span[@class="pay-price"]/text()')[0].strip()


