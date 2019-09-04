from lxml import etree
import requests
url='https://baike.baidu.com/pic/%E5%BE%B7%E7%8E%9B%E8%A5%BF%E4%BA%9A%E4%B9%8B%E5%8A%9B/7087378/0/203fb80e7bec54e7d033a232b4389b504fc26a3b?fr=lemma&ct=single#aid=0&pic=203fb80e7bec54e7d033a232b4389b504fc26a3b'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).content
tree = etree.HTML(response)
img = tree.xpath('//div[@id="picture"]/img/@src')[0]
# href = img.attrib.get('src')
print(img)
picture = requests.get(url=img).content#
with open('z_y_g1.jpg','wb' ) as fp:
    fp.write(picture)# 有错
    fp.close()
