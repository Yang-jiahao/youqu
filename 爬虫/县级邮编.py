'''
import requests
from lxml import etree

url = 'http://www.1234i.com/ybqh/'
proxies = {
    'http':'http://163.204.242.57:9999'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,proxies=proxies).content.decode('gb2312','ignore')
print(response)
shengfen = etree.HTML(response)
print(shengfen)
sheng = shengfen.xpath('//table[3]//a/@href')
print(sheng)
print(len(sheng))
for i in sheng:
    print(type(i))
    url_s = 'http://www.1234i.com/ybqh/{}'.format(i)
    responses = requests.get(url=url_s,proxies=proxies).content.decode('gb2312','ignore')
    ids = etree.HTML(responses)
    print(responses)
    qu = ids.xpath('.//table[last()]/td[@width="45%"]/center/text()')
    youid = ids.xpath('.//table[last()]/td[@width="16%"]/center/text()')
    print(qu,youid)
'''

'''
import requests
from lxml import etree
url = 'https://www.youbianku.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).text
shengfen = etree.HTML(response)

sheng = shengfen.xpath('//table[@width="336"]//tr/td/a/text()')
print(sheng)

for i in sheng:
    urls = 'https://www.youbianku.com/'+i
    responses = requests.get(url=urls,headers=headers).text
    cy = etree.HTML(responses)
    you = cy.xpath('//table//tr//p/a/text()')
    for x in you[1::3]:
        print(x)
        print('-------------------')
'''

import requests
import re
from lxml import etree
url = 'https://www.youbianku.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).text
shengfen = etree.HTML(response)

sheng = shengfen.xpath('//table[@width="336"]//tr/td/a/text()')
# 上面没错

for i in sheng:
    urls = 'https://www.youbianku.com/%s'%i
    responses = requests.get(url = urls,headers=headers).text
    # print(responses)
    xuqiu = re.compile(r'<table style="width:100%; border:1px solid #cedff2;background-color:#f5faff;border-collapse:collapse; text-align: center;" border="1">.*?电话区号.*?</tr>(.*?)</table>',re.S)
    libiao = xuqiu.findall(responses)
    for x in libiao:
        youbian = re.compile('<p><a href="/.*?>(.*?)</a>.*?</p>',re.S)
        xiang = youbian.findall(x)
        print(xiang[0::2])
        print(xiang[1::3])

