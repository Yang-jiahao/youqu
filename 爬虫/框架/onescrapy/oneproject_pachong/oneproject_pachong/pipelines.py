# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json


class OneprojectPachongPipeline(object):
    def __init__(self):
        super().__init__()
        self.flie=open('meiju.json','wb')
        self.lis=[]
        # 应该是执行的这个类,一次次的执行
    def process_item(self, item, spider):
        # 管道
        # 这里管着是否存入数据库，前面的items只是定义格式.想启用，必须在setting中设置
        json.dump(dict(item),open('meiju.json','a',encoding='utf-8'),ensure_ascii=False)
        print('=============+写入成功+===============')
        return item

'''
class OneprojectPachongPipeline(object):
    def __init__(self):
        super().__init__()
        self.lis=[]
    def process_item(self, item, spider):
        # 管道
        # 这里管着是否存入数据库，前面的items只是定义格式.想启用，必须在setting中设置
        print('=============+写入成功+===============')
        return item
'''