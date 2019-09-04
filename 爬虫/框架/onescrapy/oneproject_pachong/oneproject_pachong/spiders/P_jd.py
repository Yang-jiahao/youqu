# -*- coding: utf-8 -*-
import scrapy


class PJdSpider(scrapy.Spider):
    name = 'P_jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
