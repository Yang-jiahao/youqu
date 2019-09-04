import os
import time
import requests
import pymysql
from lxml import etree
from selenium import webdriver
if os.path.exists('链家/链家'):
    pass
else:
    os.mkdir('链家/链家')

# 定义数据库
class mysqls:
    def __init__(self):
        self.connect=pymysql.connect(
            host='localhost',
            db='test',
            user='root',
            password='456'
        )
        self.cursor=self.connect.cursor()
    def save_sql(self,image,namez,leixing,quyu,shangqu,huxing,z_price,xiangmudizhi,shouloudizhi,kaifashang,wuye,zuixinkaipan,jiaofangshijian,chanquannianxian,guihuahushu,rongjilv,lvhua):
        sal='insert into test(image,namex,leixing,quyu,shangqu,huxing,z_price,xiangmudizhi,shouloudizhi,kaifashang,wuye,zuixinkaipan,jiaofangshijian,chanquannianxian,guihuahushu,rongjilv,lvhua) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sal,(image,namez,leixing,quyu,shangqu,huxing,z_price,xiangmudizhi,shouloudizhi,kaifashang,wuye,zuixinkaipan,jiaofangshijian,chanquannianxian,guihuahushu,rongjilv,lvhua))
        self.connect.commit()
        return '保存成功'

# 保存列表页面
"""
for i in range(1,18):
    url = 'https://bj.fang.lianjia.com/loupan/pg%d/'%i
    response = requests.get(url=url).text
    print(i)
    with open('链家/%d.html'%i,'w',encoding='utf-8') as fp:
        fp.write(response)
"""
# 列表页
def lianjie():
    count=0
    for x in range(1,18):
        if os.path.exists('链家/%d'%x):
            pass
        else:
            os.mkdir('链家/%d'%x)
        lie = open('链家/%d.html' % x, 'r', encoding='utf-8')
        page = lie.read()
        tree = etree.HTML(page)
        li_list=tree.xpath('//li[@class="resblock-list post_ulog_exposure_scroll has-results"]')
        for li in li_list:
            image = li.xpath('./a/img/@data-original')[0]#图片
            namez = li.xpath('.//a[@class="name "]/text()')[0]#小区名
            leixing = li.xpath('//span[@class="resblock-type"]/text()')[0]#类型
            jianzhumianji=li.xpath('.//div[@class="resblock-area"]//text()')[1]
            # a_price=li.xpath()
            quyu = li.xpath('//div[@class="resblock-location"]/span[1]/text()')[0]#区域
            shangqu=li.xpath('//div[@class="resblock-location"]/span[2]/text()')[0]#商圈
            huxing=li.xpath('//a[@class="resblock-room"]/span/text()')[0]#户型
            # price=li.xpath('//div[@class="main-price"]/span[1]/text()')#价格
            z_price=li.xpath('//div[@class="second"]/text()')[0]#总价
            print(image,namez,leixing,quyu,shangqu,huxing,z_price)

            href = li.xpath('./a/@href')[0]
            # url = 'https://bj.fang.lianjia.com' + href
            # response = requests.get(url=url).text
            # fangyuang = etree.HTML(response)
            # time.sleep(5)
            # with open('链家/%d/%s.html'%(x,name),'w',encoding='utf-8') as fp:
            #     fp.write(response)
            lie = open('链家/%d/%s.html' %(x,namez), 'r', encoding='utf-8')
            lie = etree.HTML(lie.read())
            xiangmudizhi = lie.xpath('//p[@class="desc-p clear"][1]/span[@class="label-val"]/text()')[0]
            shouloudizhi = lie.xpath('//p[@class="desc-p clear"][2]/span[@class="label-val"]/text()')[0]
            kaifashang = lie.xpath('//p[@class="desc-p clear"][3]/span[@class="label-val"]/text()')[0]
            wuye = lie.xpath('//p[@class="desc-p clear"][4]/span[@class="label-val"]/text()')[0]
            zuixinkaipan = lie.xpath('.//li[@class="odd"][1]//span[@class="label-val"]//text()')[0]
            jiaofangshijian = lie.xpath('.//ul[@class="table-list clear"]/li[@class="odd"][2]/p/span[@class="label-val"]/text()')[0]
            chanquannianxian = lie.xpath('.//ul[@class="table-list clear"]/li[@class="odd"][3]/p/span[@class="label-val"]/text()')[0]
            guihuahushu = lie.xpath('.//ul[@class="table-list clear"]/li[@class="odd"][4]/p/span[@class="label-val"]/text()')[0]
            rongjilv = lie.xpath('.//ul[@class="table-list clear"]/li[@class="even"][1]/p/span[@class="label-val"]/text()')[0]
            lvhua = lie.xpath('.//ul[@class="table-list clear"]/li[@class="even"][2]/p/span[@class="label-val"]/text()')[0]
            lvhua_z=lvhua.strip()
            print(xiangmudizhi,shouloudizhi,kaifashang,wuye)
            print(zuixinkaipan,jiaofangshijian,chanquannianxian,guihuahushu,rongjilv,lvhua.strip())
            mysqls().save_sql(image,namez,leixing,quyu,shangqu,huxing,z_price,xiangmudizhi,shouloudizhi,kaifashang,wuye,zuixinkaipan,jiaofangshijian,chanquannianxian,guihuahushu,rongjilv,lvhua_z)
            # print(jianzhumianji)
            # print(href)
            count+=1
    print(count)

if __name__ == '__main__':
    lianjie()