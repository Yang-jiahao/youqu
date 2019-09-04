import requests
from lxml import etree
url='https://api.bilibili.com/x/v1/dm/list.so?oid=31621681'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).content
tree = etree.HTML(response)

danmu = tree.xpath('//d/text()')
for i in danmu:
    y=i+'\n'
    with open('bilibili.txt','a',encoding='utf-8') as fp:
        fp.write(y)
