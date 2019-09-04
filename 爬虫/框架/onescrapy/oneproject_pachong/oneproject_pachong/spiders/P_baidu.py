# -*- coding: utf-8 -*-
import scrapy


class PBaiduSpider(scrapy.Spider):
    name = 'P_baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # print(response.body.decode('utf-8'))
        with open('百度首页.html','w',encoding=('utf-8'))as fp:
            fp.write(response.body.decode('utf-8'))