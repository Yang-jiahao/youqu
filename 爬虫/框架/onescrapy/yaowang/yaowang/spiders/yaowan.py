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
            pricez=li.xpath('./div[position()=1]/p[@class="price"]//text()')
            price=''.join(pricez).strip()
            href=li.xpath('./div[position()=1]//img/@src')[0]
            urlx1=li.xpath('./div[position()=1]/a/@href')[0]
            urlx='https:'+urlx1
            store=li.xpath('./div[position()=1]/div[@class="sell_type_div"]/span[last()]//text()')[0]
            yaowan['title']=title
            yaowan['price']=price
            yaowan['href']=href
            yaowan['store']=store
            yaowan['urlx']=urlx
            yield scrapy.Request(url=urlx,callback=self.parse_d,meta={'data':yaowan})

    def parse_d(self,response):
        yaowan=response.meta['data']
        print(yaowan)
        intree=etree.HTML(response.body.decode('gbk'))

        brand=intree.xpath('//div[@class="goods_intro"]//tr[1]/td/text()')[0]
        sizes=intree.xpath('//div[@class="goods_intro"]//tr[2]/td[2]/text()')[0]
        weights=intree.xpath('//div[@class="goods_intro"]//tr[3]/td[1]/text()')[0]
        manufacturer=intree.xpath('//div[@class="goods_intro"]//tr[3]/td[2]/text()')[0]
        approval=intree.xpath('//div[@class="goods_intro"]//tr[4]/td[1]//text()')
        approval_number=''.join(approval).strip()
        yaowan['brand']=brand
        yaowan['sizes']=sizes
        yaowan['weights']=weights
        yaowan['manufacturer']=manufacturer
        yaowan['approval_number']=approval_number
        # with open('详情.html','w',encoding='utf-8')as fp:
        #     fp.write(response.body.decode('gbk'))
        yield yaowan