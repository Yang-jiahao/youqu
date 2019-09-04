# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import OneprojectPachongItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        html=response.body.decode('gb2312')
        tree=etree.HTML(html)
        li_list=tree.xpath('//ul[@class="top-list  fn-clear"]/li')
        for li in li_list:
            #实例化一个文档
            wendang=OneprojectPachongItem()

            rank=li.xpath('.//i/text()')[0]
            title=li.xpath('./h5/a/text()')[0]
            states=li.xpath('./span[1]//text()')[:2]
            state=''.join(states)
            types=li.xpath('./span[2]//text()')[0]
            tv=li.xpath('./span[3]//text()')[0]
            uptimes=li.xpath('.//div[@class="lasted-time new100time fn-right"]//text()')
            uptime=''.join(uptimes)

            # 保存到文档,
            wendang['rank']=rank
            wendang['title']=title
            wendang['state']=state
            wendang['types']=types
            wendang['tv']=tv
            wendang['uptime']=uptime

            # 暂时挂起，保存上一次操作状态
            yield wendang