from lxml import etree
import requests
import os,json

if os.path.exists('qiushi'):
    pass
else:
    os.mkdir('qiushi')
count = 0
duanzi_list =[]
for x in range(1,14):
    url = 'https://www.qiushibaike.com/8hr/page/%d/'%x
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url,headers=headers).text
    # print(response)
    qiushi = etree.HTML(response)#先html字符串转化成xml格式，然后将xml进行切分
    duanzibiao = qiushi.xpath('//div[@class="recommend-article"]/ul/li')
    # print(duanzibiao)
    count += 1
    print(count)
    for i in duanzibiao:
        duanzi = {}
        try:
            title = i.xpath('./div[@class="recmd-right"]/a[@class="recmd-content"]/text()')[0]
        except:
            title = '标题不规范'
        print(title)
        duanzi['title'] = title

        zan = i.xpath('.//span[1]/text()')[0]
        print(zan)
        duanzi['zan'] = zan

        try:
            pl = i.xpath('.//div[@class="recmd-num"]/span[last()-1]/text()')[0]
            print(pl)
        except:
            pl = '0'
            print(pl)
        duanzi['pl'] = pl

        autor = i.xpath('.//a[@class="recmd-user"]/img/@alt')[0]
        print(autor)

        duanzi['autor'] = autor
        duanzi_list.append(duanzi_list)
        print(count)
        print('===========================================')
        with open('qiushi/duanzi.json','a',encoding='utf-8') as fp:
            json.dump(duanzi,fp,ensure_ascii=False)
