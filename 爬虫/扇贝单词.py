import requests
from lxml import etree
for x in range(1,4):
    url = f'https://www.shanbay.com/wordlist/110521/232414/?page={x}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url,headers=headers).text
    # with open('扇贝.html','w',encoding='utf-8') as fp:
    #     fp.write(response)
    shanbei = etree.HTML(response)
    print(shanbei)
    td_list = shanbei.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for td in td_list:
        # print(td)
        word = td.xpath('.//td[@class="span2"]/strong/text()')[0]
        print(word)

        tranlate = td.xpath('.//td[@class="span10"]/text()')[0]
        print(tranlate)
        shanbei_word = word+','+tranlate+'\n'
        with open('扇贝单词.txt','a',encoding='utf-8') as fp:
            fp.write(shanbei_word)
        print('----------------------------------------------')

