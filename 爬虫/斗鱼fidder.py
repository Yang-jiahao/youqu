import requests
import json
from lxml import etree
from selenium import webdriver


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
url = 'https://www.douyu.com/gapi/rkc/directory/0_0/1'
xman_json = requests.get(url=url).json()
page_num=xman_json['data']['pgcnt']
num=xman_json['data']['rl']
# 使用fidder的时候会优先使用fidder，然后再进入chrome

a=[]
for i in range(1,page_num):
    urlz='https://www.douyu.com/gapi/rkc/directory/0_0/%d'%i
    running_json=requests.get(url=urlz).json()
    rl = running_json['data']['rl']
    for x in range(len(rl)):
        title=running_json['data']['rl'][x]['rn']
        name=running_json['data']['rl'][x]['nn']
        type=running_json['data']['rl'][x]['c2name']
        hot=running_json['data']['rl'][x]['ol']
        dic={}
        dic['title']=title
        dic['name']=name
        dic['type']=type
        dic['hot']=hot
        a.append(dic)
with open('douyu.json','w',encoding='utf-8') as fp:
    fp.write(a)

