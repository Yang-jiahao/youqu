import requests
import re

url = 'https://www.qiushibaike.com/8hr/page/1/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
yemian = requests.get(url=url,headers=headers).text
# print(yemian)
# yemian_rule = re.compile(r'<div class="recmd-right">(.*?)</div>',re.S)
# result = yemian_rule.findall(yemian)
page_rule = re.compile(r'<span class="page-numbers">\s(.*?)\s</span>',re.S)
page = page_rule.findall(yemian)
p = page[len(page)-1]

p = int(p)
for x in range(1,p+1):
    urls = f'https://www.qiushibaike.com/8hr/page/{x}/'
    yes = requests.get(url=urls,headers=headers).text
    yes_rule = re.compile(r'<div class="recmd-right">(.*?)</div>',re.S)
    result = yes_rule.findall(yes)
    for i in result:
        title_rule = re.compile(r'>(.*?)</a>')
        title = title_rule.findall(i)[0]


        zan_rule = re.compile(r'<span>(.*?)</span><span>好笑</span>')
        zan = zan_rule.findall(i)[0]


        pinglun_rule = re.compile(r'<span>(.*?)</span><span>评论</span>')
        pinglun = pinglun_rule.findall(i)
        print(pinglun)
        try:
            print(pinglun[0])
            xie = title+'，'+zan+'，'+pinglun[0]+'\n'
            with open('糗事百科.txt','a',encoding='utf-8') as fp:
                fp.write(xie)
        except:
            xie = title +'，'+ zan +'，'+ '0'+'\n'
            with open('糗事百科.txt', 'a', encoding='utf-8') as fp:
                fp.write(xie)
            pass
        # if pinglun is None:
        #     print(None)
        # else:
        #     print(pinglun[0])
        print('=========================================================================')
