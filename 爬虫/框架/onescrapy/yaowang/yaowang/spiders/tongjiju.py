# -*- coding: utf-8 -*-
import scrapy
from lxml import etree

class TongjijuSpider(scrapy.Spider):
    name = 'tongjiju'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html']

    def parse(self, response):
        html=response.body.decode('gb2312',errors="ignore")
        print(html)
        tree=etree.HTML(html)
        province=tree.xpath('//tr[@class="provincetr"]/td/a/@href')
        print('===========================',province)
