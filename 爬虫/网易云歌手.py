import requests
from lxml import etree
class Wangyiicloud:
    def __init__(self,url):
        self.tree = self.requests_url(url)
        self.xunhuan()

    def requests_url(self,url):
        headers =  {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url=url, headers=headers).text
        tree = etree.HTML(response)#返回一个xml
        return tree
    def xunhuan(self):
        fenzu_list = self.tree.xpath('//div[@class="blk"]//a/text()')
        fenzu_link = self.tree.xpath('//div[@class="blk"]//a/@href')
        for group, link in zip(fenzu_list, fenzu_link):
            print(group)
            # 一层页面得到地区分组
            url_link = 'https://music.163.com%s' % link
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

            names = group.replace('/', '')
            wangyi = open('网易云歌手/%s.html' % names, 'r', encoding='utf-8')
            words = etree.HTML(wangyi.read())
            name_links = words.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')  # -------
            for x in name_links:
                # 两层页面得到大写字母ABCD
                word_url = 'https://music.163.com%s' % x
                singer = requests.get(url=word_url, headers=headers).text
                name = etree.HTML(singer)
                singerlist = name.xpath(
                    '//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]//a[@class="nm nm-icn f-thide s-fc0"]/text()')
                print(singerlist)
                for n in singerlist:
                    # 三层页面得到姓名
                    nx = n + '\n'
                    with open('singer.txt', 'a', encoding='utf-8') as sn:
                        sn.write(nx)

if __name__ == '__main__':
    url = 'https://music.163.com/discover/artist/'
    Wangyiicloud(url)

"""
url = 'https://music.163.com/discover/artist/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

'''
# response = requests.get(url=url,headers=headers).text

# print(response)
# with open('quanbu.html','w',encoding='utf-8') as fp:
#     fp.write(response)

# with open('quanbu.html','r') as fp:
#     haha = fp.read()
#     print(haha)
'''

f = open('quanbu.html','r',encoding='utf-8')
fenzu = etree.HTML(f.read())
print(fenzu)
fenzu_list = fenzu.xpath('//div[@class="blk"]//a/text()')
fenzu_link = fenzu.xpath('//div[@class="blk"]//a/@href')
count = 0
for group,link in zip(fenzu_list,fenzu_link):
    print(group)
    # 一层页面得到地区分组
    url_link = 'https://music.163.com%s' % link
    names_html = requests.get(url=url_link, headers=headers).text
    names = group.replace('/','')
    wangyi = open('网易云歌手/%s.html'%names,'r',encoding='utf-8')
    words = etree.HTML(wangyi.read())
    name_links =words.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')#-------
    for x in name_links:
        #两层页面得到大写字母ABCD
        word_url = 'https://music.163.com%s'%x
        singer = requests.get(url=word_url,headers=headers).text
        name = etree.HTML(singer)
        singerlist = name.xpath('//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]//a[@class="nm nm-icn f-thide s-fc0"]/text()')
        print(singerlist)
        for n in singerlist:
            # 三层页面得到姓名
            nx = n+'\n'
            with open('singer.txt','a',encoding='utf-8') as sn:
                sn.write(nx)
            count+=1
print(count)

"""