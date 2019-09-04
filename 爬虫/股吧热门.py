import requests
from lxml import etree
count = 0
for i in range(1,13):
    url = f'http://guba.eastmoney.com/default,99_{i}.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url,headers).text
    guba = etree.HTML(response)
    guba_lists = guba.xpath('//ul[@class="newlist"]/li')
    for x in guba_lists:

        yuedu = x.xpath('.//cite[1]/text()')[0].strip()
        print(yuedu)

        pinglun = x.xpath('.//cite[2]/text()')[0].strip()
        print(pinglun)

        try:
            baname = x.xpath('.//span/a[@class="balink"]/text()')[0]
            print(baname)
        except:
            baname='一鸣'
            print(baname)

        title = x.xpath('.//span/a/text()')[0]
        print(title)

        autor = x.xpath('.//font/text()')[0]
        print(autor)

        times = x.xpath('.//cite[4]/text()')[0]
        print(times)

        tie = yuedu+','+pinglun+','+baname+','+title+','+autor+','+times+'\n'
        with open('股吧热门.txt','a',encoding='utf-8') as fp:
            fp.write(tie)
        count+=1
print(count)