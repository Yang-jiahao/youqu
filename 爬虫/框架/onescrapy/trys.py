import requests
from lxml import etree
url='https://www.xin.com/beijing/i1/?channel=a49b117c44837d110753e751863f53'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response=requests.get(url=url,headers=headers).content.decode('utf-8')
res = response
print(res)
tree = etree.HTML(res)
li_list=tree.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
for li in li_list:
    print('123321')
    title = li.xpath('//h2/span/text()')[0]
    price = li.xpath('//div[@class="across"]//em/text()')[0].strip()
    gongli = li.xpath('//div[@class="pad"]/span//text()')[2:4]
    cangku = li.xpath('//div[@class="pad"]/span/span/text()')
    age = li.xpath('//div[@class="pad"]//span/text()[1]')
    img = li.xpath('//img/@data-original')
    renzheng = li.xpath('//span[@class="caritem-icon yxrz-icon"]//text()[last()]')
    shoufu = li.xpath('//span[@class="pay-price"]/text()')[0].strip()

    print(title)
    print(price)
    print(gongli)
    print(cangku)
    print(age)
    print(img)
    print(renzheng)
    print(shoufu)
