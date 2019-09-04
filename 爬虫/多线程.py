import requests
import json,time
import threading
from queue import Queue

class TX(threading.Thread):
    def __init__(self,i,qq):
        super().__init__()
        self.i=i
        self.qq=qq

    def run(self):
        while True:
            if self.qq.empty():
                break
            page=self.qq.get()
            print(f'================={self.i}执行{page}================')
            url=f'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex={page}&pageSize=10&language=zh-cn&area=cn'
            self.txzp(url)
            print(f'================={self.i}over{page}================')

    def txzp(self,url):
        headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url=url,headers=headers).json()
        # with open('tx.json','w',encoding='utf-8') as fp:
        #     fp.write(response)
        self.dujson(response)

    def dujson(self,response):
        obj_list=response['Data']['Posts']
        for info in obj_list:
            name=info['RecruitPostName']
            add=info['LocationName']
            zz=info['Responsibility'].replace('\n','').replace('\r','')
            PostURL=info['PostURL']
            job=f'{name}{add}{zz}{PostURL}'+'\n'
            with open('腾讯招聘.txt','a',encoding='utf-8') as fp:
                fp.write(job)


if __name__ == '__main__':
    start=time.time()
    queues=Queue()
    for i in range(1,11):
        queues.put(i)
    c=['c1','c2','c3']
    x=[]
    for i in c:
        aa=TX(i=i,qq=queues)
        aa.start()
        x.append(aa)
    # 这个启动起来以后县城并没有执行完成，只是并行跑起来了
    for zuse in x:
        # 然后在这里喊了一句，劳资不执行完，管事的不能走
        zuse.join()
    endding=time.time()
    print(endding-start)
