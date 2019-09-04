# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import YaowangItem
class YaowanSpider(scrapy.Spider):
    name = 'yaowan'
    allowed_domains = ['111.com.cn']
    start_urls = []
    for i in range(1,5):
        url=f'https://www.111.com.cn/categories/953710-j{i}.html'
        start_urls.append(url)
    def parse(self, response):
        html=response.body.decode('gbk')
        tree=etree.HTML(html)
        li_list=tree.xpath('//ul[@id="itemSearchList"]/li')
        for li in li_list:
            yaowan=YaowangItem()
            title=li.xpath('./div[position()=1]/p[@class="titleBox"]/a//text()[last()]')[0].strip()
            price=li.xpath('./div[position()=1]/p[@class="price"]//text()')[2].strip()
            href=li.xpath('./div[position()=1]//img/@src')[0]
            store=li.xpath('./div[position()=1]/div[@class="sell_type_div"]/span[last()]//text()')[0]
            yaowan['title']=title
            yaowan['price']=price
            yaowan['href']=href
            yaowan['store']=store
            yield yaowan

