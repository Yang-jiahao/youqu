from lxml import etree
import requests
url = 'https://maoyan.com/board'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).text
with open('maoyan.html','w',encoding='utf-8') as fp:
    fp.write(response)
    # 查看保存下来的数据是否与原来的页面一致
xmls = etree.HTML(response)
dd_list = xmls.xpath('//dd')
for i in dd_list:
    # print(i)
    rank = i.xpath('./i[1]/text()')[0]
    print(rank)

    images = i.xpath('.//a/img[2]/@data-src')[0]
    # src为什么获取不到
    # 其实保存的图片的连接属性是data-src就是说保存下来的是一个会变的数据
    print(images)

    # name = i.xpath('./a/@title')[0]
    name = i.xpath('.//p[@class="name"]/a/text()')[0]
    print(name)

    actors = i.xpath('.//p[@class="star"]/text()')[0].strip()
    print(actors)

    score = i.xpath('.//p[@class="score"]/i/text()')
    score_enmmm=''.join(score)
    print(score_enmmm)

