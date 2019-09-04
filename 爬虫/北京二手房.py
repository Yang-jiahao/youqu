import requests,os,time
from lxml import etree
import random

if os.path.exists('北京二手房'):
    pass
else:
    os.mkdir('北京二手房')

"""
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
# u='https://esf.fang.com/house/'
# one = requests.get(url=u,headers=headers).text
# with open('北京二手房/1.html','w',encoding='utf-8') as fpx:
#     fpx.write(one)

pro=[
        'https://175.43.34.31:9999',
        'https://112.87.68.188:9999',
        'https://120.83.97.75:9999',
        'https://114.106.156.52:808',
        'https://120.83.110.132:9999',
        'https://123.163.122.115:9999',
        'https://182.34.35.21:9999',
        'https://59.57.148.112:9999',
        'https://113.124.94.96:9999',
        'https://163.204.246.163:9999',
        'https://182.34.35.93:9999',
        'https://113.121.22.39:9999',
        'https://58.253.158.148:9999'
    ]

for i in range(2,101):
    a='3'+str(i)
    url='https://esf.fang.com/house/i%s/'%a
    response = requests.get(url=url,headers=headers,proxies={'https':random.choice(pro)}).text
    with open('北京二手房/%d.html'%i, 'w', encoding='utf-8') as fpx:
        fpx.write(response)
    print(i)
    suiji = random.randint(5,10)
    time.sleep(suiji)
print(random.random())#0-1秒小数
print(random.randint(5,10))#生成一个随机时间
"""

diyiye = open('北京二手房/1.html','r',encoding='utf-8')
tree = etree.HTML(diyiye.read())
dd=tree.xpath('//dl[@id="kesfqbfylb_A01_01_03"]')
for d in dd:
    title = d.xpath('//span[@class="tit_shop"]/text()')#标题
    xiaoqu = d.xpath('//p[@class="add_shop"]/a/@title')#小区
    dizhi = d.xpath('//p[@class="add_shop"]/span/text()')#地址
    people = d.xpath('//span[@class="people_name"]/a/text()')#经理
    price = d.xpath('//span[@class="red"]/b/text()')#总价格
    for q,w,e,r,t in zip(title,xiaoqu,dizhi,people,price):
        print(q)
        print(w)
        print(e)
        print(r)
        print(t)




