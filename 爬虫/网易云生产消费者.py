import time
import requests
import threading
from queue import Queue
from lxml import etree

# 1是作为请求所有的分类
class FenQu(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        self.qingFen()
    def qingFen(self):
        url='https://music.163.com/discover/artist/'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response =requests.get(url=url,headers=headers).text
        tree=etree.HTML(response)
        fenzu_link = tree.xpath('//div[@class="blk"]//a/@href')
        for i in fenzu_link:
            f_queue.put(i)#地区分组结束,url拿到


# 2是请求每一个详细的分页,ABCD...
class Diqu(threading.Thread):
    def __init__(self,f_queue):
        super().__init__()
        self.f_queue=f_queue
    def run(self):
        while True:
            if self.f_queue.empty():
                break
            try:
                link=self.f_queue.get(block=False)#本来呢默认取数据的时候是阻塞式的，加上这个flase就成了不阻塞了
                self.qingYe(link)
            except:
                pass
    def qingYe(self,link):
        # 每一个ABCD等等
        url_link = 'https://music.163.com%s'%link
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        text = requests.get(url=url_link, headers=headers).text
        words = etree.HTML(text)
        name_links = words.xpath('//ul[@id="initial-selector"]/li[position()>1]/a/@href')
        for x in name_links:
            z_queue.put(x)

# 3是将请求写下来
class ZiMu(threading.Thread):
    def __init__(self,z_queue):
        super().__init__()
        self.z_queue=z_queue
    def run(self):
        while True:
            if self.z_queue.empty() and flag:
                break
            try:
                zm_link=self.z_queue.get(block=False)
                self.zimu(zm_link)
            except:
                pass
    def zimu(self,zm_link):
        word_url = 'https://music.163.com%s' % zm_link
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        singer = requests.get(url=word_url, headers=headers).text
        name = etree.HTML(singer)
        singerlist = name.xpath('//ul[@class="m-cvrlst m-cvrlst-5 f-cb"]//a[@class="nm nm-icn f-thide s-fc0"]/text()')
        for i in singerlist:
            aya=i+'\n'
            with lock:
                with open('网易云音乐生产消费者.txt', 'a', encoding='utf-8') as fp:
                    fp.write(aya)



lock=threading.Lock()
fal=False
if __name__ == '__main__':
    start=time.time()
    f_queue = Queue()
    z_queue=Queue()
    FenQu()

    '''
    Diqu(f_queue)
    ZiMu(z_queue)
    这样仅仅把线程启动了一遍
    '''

    diqu=[]
    for i in range(5):
        d=Diqu(f_queue)
        d.start()
        diqu.append(d)

    zimus=[]
    # 这个range到底取多少
    for w in range(26):
        z=ZiMu(z_queue)
        z.start()
        zimus.append(z)

    for x in diqu:
        x.join()

    flag=True#这标志着第一个线程项目全部down掉了

    for o in zimus:
        o.join()
    ens=time.time()
    print(ens-start)
    # 此时第二个线程项目去阻塞主线程