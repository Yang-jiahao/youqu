# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
def BaoCun(title,price,href,store):
    connect=pymysql.connect(
        host='localhost',
        db='test',
        user='root',
        password='456',
    )
    cousor=connect.cursor()
    sql='insert into test(title,price,href,store) VALUE (%s,%s,%s,%s)'
    cousor.execute(sql,(title,price,href,store))
    connect.commit()


class YaowangPipeline(object):
    def process_item(self, item, spider):
        print(f'================{item}================')
        title=item['title']
        price=item['price']
        href=item['href']
        store=item['store']
        # BaoCun(title,price,href,store)
        print('================保存成功================')
        return item


class YouxinPipeline(object):
    def process_item(self, item, spider):
        pass

class TongjijuPipeline(object):
    def process_item(self, item, spider):
        pass