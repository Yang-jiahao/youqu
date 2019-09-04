import time
import requests
import os,time,random
import pymysql
from lxml import etree
# from fake_useragent import UserAgent#默认使用一个代理浏览器,这个浏览器代理是自动生成的

if os.path.exists('安居客'):
    pass
else:
    os.mkdir('安居客')

class Anjuke:
    def __init__(self,url):
        self.url = url
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        # self.headers = {'user-agent':useragent.random}
        self.citys()
        self.connect = pymysql.connect(
            host='localhost',
            db='test',
            user='root',
            password='456'
        )#连接数据库
        self.cursor = self.connect.cursor()#创建游标
        """
        cursor就是一个Cursor对象，
        这个cursor是一个实现了迭代器（def__iter__()）和生成器（yield）的MySQLdb对象，
        这个时候cursor中还没有数据，
        只有等到fetchone()或fetchall()的时候才返回一个元组tuple，
        才支持len()和index()操作，这也是它是迭代器的原因。
        但同时为什么说它是生成器呢？
        因为cursor只能用一次，即每用完一次之后记录其位置，
        等到下次再取的时候是从游标处再取而不是从头再来，而且fetch完所有的数据之后，
        这个cursor将不再有使用价值了，即不再能fetch到数据了。
        """
        pass
    def save_sql(self,img,infotitle,jingli,shi,ting,pingfang,xiaoqu,dizhi,zffs,cx,jiage):
        sql = 'insert into test(img,info,jingli,shi,ting,pingfang,xiaoqu,dizhi,zffs,chaoxiang,jiage) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        # try:
            # with open('安居库房源信息.txt', 'a', encoding='utf-8') as fpx:
            #     fpx.write(heihei)
            # 这里应该写数据库中的字段
        jl = jingli.strip()
        dz = dizhi.strip()
        self.cursor.execute(sql, (img, infotitle, jl, shi, ting, pingfang, xiaoqu, dz, zffs, cx, jiage))  # 执行插入语句
        self.connect.commit()  # 提交
        #     print('插入成功')
        # except:
        #     print('插入失败')
        #     pass

    def citys(self):
        # response_one = requests.get(url=self.url,headers = self.headers).text
        # print(response_one)
        # with open('安居客/city.html','w',encoding='utf-8') as fp:
        #     fp.write(response_one)
        anjuke = open('安居客/city.html','r', encoding='utf-8')
        tree = etree.HTML(anjuke.read())
        href_list = tree.xpath('//div[@class="letter_city"]/ul/li[position()>12 and position()<18]//a/@href')
        href_name = tree.xpath('//div[@class="letter_city"]/ul/li[position()>12 and position()<18]//a/text()')
        print(href_name)
        for link,name in zip(href_list,href_name):
            # response_link = requests.get(url=link,headers = self.headers).text
            # if os.path.exists('安居客/安居客_city'):
            #     pass
            # else:
            #     os.mkdir('安居客/安居客_city')
            # with open('安居客/安居客_city/%s.html'%name,'w',encoding='utf-8') as xp:
            #     xp.write(response_link)
            city_info_link = open('安居客/安居客_city/%s.html'%name,'r',encoding='utf-8')
            city_info = etree.HTML(city_info_link.read())
            city_list = city_info.xpath('//ul[@class="L_tabsnew"]/li[4]/a[@class="a_navnew"]/@href')
            print(city_list)
            # print(city_list)
            try:
                print(name,city_list[0])
                for pages in range(1,100):
                    #遍历的完整页面
                    page_url = city_list[0]+'fangyuan/p%d/'%pages
                    # print(page_url)
                    print(name,page_url)
                    print('============================================================')
                    try:
                        fangyuan = requests.get(url=page_url, headers=self.headers).text
                        # print(fangyuan)
                        # fangyuan = requests.get(url=page_url, headers=self.headers,proxies={'https':random.choice(pro)}).text
                        fang_tree = etree.HTML(fangyuan)
                        # print(fang_tree)
                        # ================================再一次写了一个遍历单一li的项目========================================
                        xiangxi = fang_tree.xpath('//div[@class="zu-itemmod"]')
                        print(xiangxi)
                        # 完整页面中切出来小盒子的列表
                        for mx in xiangxi:
                            # 遍历的一个页面中的所有的小盒子
                            # 遍历每一个盒子中的信息
                            img_list = mx.xpath('//img/@src')
                            infotitle_list = mx.xpath('//div[@class="zu-info"]/h3//b[1]/text()')
                            shi_list = mx.xpath('//div[@class="zu-info"]/p[1]/b[1]/text()')
                            ting_list = mx.xpath('//div[@class="zu-info"]/p[1]/b[2]/text()')
                            pingfang_list = mx.xpath('//div[@class="zu-info"]/p[1]/b[3]/text()')
                            louceng_list = mx.xpath('//p[@class="details-item tag"]/text()[5]')
                            jingli_list = mx.xpath('//p[@class="details-item tag"]/text()[6]')
                            xiaoqu_list = mx.xpath('//address[@class="details-item"]/a/text()')
                            dizhi_list =mx.xpath('//address[@class="details-item"]//text()[2]')
                            zffs_list = mx.xpath('//p[@class="details-item bot-tag"]/span[1]/text()')
                            cx_list = mx.xpath('//p[@class="details-item bot-tag"]/span[2]/text()')
                            jiage_list = mx.xpath('//div[@class="zu-side"]//b[@class="strongbox"]/text()')
                            print('可以是zip')
                            for img, infotitle, jingli, shi, ting, pingfang, xiaoqu, dizhi, zffs, cx, jiage in zip(img_list, infotitle_list, jingli_list, shi_list, ting_list, pingfang_list, xiaoqu_list, dizhi_list, zffs_list, cx_list, jiage_list):
                                print('>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:》')
                            # print(dix)
                            # print(img)
                                heihei= '%s|'%name+'{},{},{},{},{},{},{},{},{},{},{},\n'.format(img,infotitle,jingli,shi,ting,pingfang,xiaoqu,dizhi,zffs,cx,jiage)
                                # print(heihei)
                                self.save_sql(img,infotitle,jingli,shi,ting,pingfang,xiaoqu,dizhi,zffs,cx,jiage)

                        '''
                                                try:
                            img = fang_tree.xpath('//div[@class="zu-itemmod"]//img[1]/@src')#图片搞定
                            info = fang_tree.xpath('//h3//b[@class="strongbox"]/text()')#条件搞定
                            # print(info)
                            jingli = fang_tree.xpath('//p[@class="details-item tag"]/text()[6]')#经理搞定
                            # print(jingli)
                            shi = fang_tree.xpath('//p[@class="details-item tag"]/b[1]/text()')#户型搞定，室
                            ting = fang_tree.xpath('//p[@class="details-item tag"]/b[2]/text()')#户型搞定,厅
                            pingfang = fang_tree.xpath('//p[@class="details-item tag"]/b[3]/text()')#户型搞定,平方

                            xiaoqu = fang_tree.xpath('//address[@class="details-item"]/a/text()')#小区搞定
                            # print(xiaoqu)
                            dizhi= fang_tree.xpath('//address[@class="details-item"]//text()[2]')#地址搞定
                            # print(dizhi)
                            zufangfangshi = fang_tree.xpath('//p[@class="details-item bot-tag"]/span[1]/text()')#租房方式
                            # print(zufangfangshi)
                            chaoxiang = fang_tree.xpath('//p[@class="details-item bot-tag"]/span[2]/text()')#朝向
                            jiage = fang_tree.xpath('//div[@class="zu-side"]//b[@class="strongbox"]/text()')#价格
                            dix = [name,img,info,jingli,shi,ting,pingfang,xiaoqu,dizhi,zufangfangshi,chaoxiang,jiage]
                            print(pages)
                            print(dix)
                            with open('安居库房源信息.txt','a',encoding='utf-8') as fpx:
                                fpx.write(dix)
                            # print(xinxi)

                            print('====================数据库插入还少点东西=====================')
                        #     sql = 'insert into test(img,info,jingli,shi,ting,pingfang,xiaoqu,dizhi,zffs,chaoxiang,jiage) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                        # #     这里应该写数据库中的字段
                        #     self.cursor.execute(sql,(img,info,jingli,shi,ting,pingfang,xiaoqu,dizhi,zufangfangshi,chaoxiang,jiage))#执行插入语句
                        #     self.connect.commit()#提交
                        #     print('插入成功')
                        except:
                            pass
                      '''

                    except:
                        pass
                    time.sleep(3)
            except:
                print(name)
            """
                        try:
                print(name,city_list[0])
                responses=requests.get(url=city_list[0],headers=self.headers).text
                pages = etree.HTML(responses)
                zufang_link = pages.xpath('//a[@class="aNxt"]/@href')[0]
                for i in range(1,500):
                    meiyiye = requests.get(url=zufang_link,headers=self.headers).text
                    mei = etree.HTML(meiyiye)
                    mei.xpath('')

                print(zufang_link)
                tihuan = zufang_link[-2]
                print(zufang_link.repalce(tihuan,'======'))
                print(tihuan)
            except:
                print(name)
                pass
            # for city in city_list:
                # city_link = requests.get(url=city, headers=self.headers).text
           """





if __name__ == '__main__':
    # pro=[
    #     '175.43.34.31:9999',
    #     '112.87.68.188:9999',
    #     '120.83.97.75:9999',
    #     '114.106.156.52:808',
    #     '120.83.110.132:9999',
    #     '123.163.122.115:9999',
    #     '182.34.35.21:9999',
    #     '59.57.148.112:9999',
    #     '113.124.94.96:9999',
    #     '163.204.246.163:9999',
    #     '182.34.35.93:9999',
    #     '113.121.22.39:9999',
    #     '58.253.158.148:9999'
    # ]
    url = 'https://www.anjuke.com/sy-city.html'
    time.localtime()
    # useragent = UserAgent()
    Anjuke(url)