# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import DoubanItem
class DushuSpider(scrapy.Spider):
    name = 'dushu'
    allowed_domains = ['douban.com']
    start_urls = []
    for i in range(0,1):
        urlz='https://book.douban.com/subject_search?search_text=python&cat=1001&tdsourcetag=s_pctim_aiomsg&qq-pf-to=pcqq.group&start=0'
        start_urls.append(urlz)
        print('请求了')
    def parse(self, response):
        print('请求完成了')
        html=response.body.decode('utf-8')
        # x=response.url这个就是请求的哪个url
        tree=etree.HTML(html)
        d_list=tree.xpath('//div[@class="detail"]')
        for d in d_list:
            item=DoubanItem()
            xiaourl=d.xpath('.//div[@class="title"]/a/@href')[0]
            b_name=d.xpath('.//div[@class="title"]/a/text()')[0]
            score=d.xpath('.//div[2]/span[2]/text()')[0]
            item['xiaourl']=xiaourl
            item['b_name']=b_name
            item['score']=score
            print(xiaourl)
            yield scrapy.Request(url=xiaourl,callback=self.parse_xq,meta={'ph':False,'data':item},dont_filter=True)
    def parse_xq(self,response):
        item=response.meta['data']
        tree = etree.HTML(response.body.decode('utf-8'))

        author = tree.xpath('//div[@id="info"]/span[1]/a/text()')[0]
        publisher = tree.xpath('//div[@id="info"]//text()')
        gu_fast = tree.xpath('//div[@id="info"]//text()')
        translator = tree.xpath('//div[@id="info"]//text()')
        publication = tree.xpath('//div[@id="info"]//text()')
        page = tree.xpath('//div[@id="info"]//text()')
        price = tree.xpath('//div[@id="info"]//text()')
        paperback = tree.xpath('//div[@id="info"]//text()')
        collection = tree.xpath('//div[@id="info"]//text()')
        print(collection)
        item['author']=author
        item['publisher']=publisher
        item['gu_fast']=gu_fast
        item['translator']=translator
        item['publication']=publication
        item['page']=page
        item['price']=price
        item['paperback']=paperback
        item['collection']=collection
        yield item