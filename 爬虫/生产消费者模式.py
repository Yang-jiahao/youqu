import requests
import threading
from queue import Queue

'''
# 生产了10个吃了4个,有问题
class Project(threading.Thread):
    # 生产者
    def __init__(self,i,p_queue):
        super().__init__()
        self.i=i
        self.pqueue=p_queue
    def run(self):
        while True:
            if self.pqueue.empty():
                break
            q=self.pqueue.get()#获取队列的队尾一项，也就是出队
            url = f'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex={q}&pageSize=10&language=zh-cn&area=cn'
            print(f'+++++++++++++++++++{self.i}走+++++++++++++++++++')
            self.to_requests(url=url)
            print(f'+++++++++++++++++++{self.i}完+++++++++++++++++++')
    def to_requests(self,url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response=requests.get(url=url,headers=headers).json()
        c_queue.put(response)


class Consumer(threading.Thread):
    def __init__(self,i):
        super().__init__()
        self.i=i
    def run(self):
        while True:
            if c_queue.empty() and flag:
                break
            response = c_queue.get()
            print(f'===================={self.i}走=====================')
            self.to_project(response)
            print(f'===================={self.i}完=====================')
    def to_project(self,response):
        obj_list = response['Data']['Posts']
        for info in obj_list:
            name = info['RecruitPostName']
            add = info['LocationName']
            zz = info['Responsibility'].replace('\n', '').replace('\r', '')
            PostURL = info['PostURL']
            job = f'{name}{add}{zz}{PostURL}' + '\n'
            with open('腾讯招聘生产消费者.txt', 'a', encoding='utf-8') as fp:
                fp.write(job)
p_queue = Queue()
c_queue = Queue()
flag=False
if __name__=="__main__":

    for i in range(1,11):
        p_queue.put(i)

    p_name = ['p1','p2','p3']
    c_name=['c1','c2','c3']

    p_tread=[]
    c_tread=[]

    for i in p_name:
        p_s=Project(i,p_queue)
        p_s.start()
        p_tread.append(p_s)
    for j in c_name:
        c_x=Consumer(j)
        c_x.start()
        c_tread.append(c_x)
    flag=True
'''


class Product(threading.Thread):
    def __init__(self,i,p_queue):
        super().__init__()
        self.i=i
        self.p_queue=p_queue
    def run(self):
        while True:
            if self.p_queue.empty():
                break
            try:
                q=self.p_queue.get(block=False)
                url = f'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex={q}&pageSize=10&language=zh-cn&area=cn'
                print(f'================={self.i}走=======================')
                self.get_response(url)
                print(f'================={self.i}完=======================')
            except:
                pass
    def get_response(self,url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response = requests.get(url=url,headers=headers).json()
        c_queue.put(response)

class Consumer(threading.Thread):
    def __init__(self,i):
        super().__init__()
        self.i=i
    def run(self):
        while True:
            if c_queue.empty() and flag:
                break
            try:
                response=c_queue.get(block=False)
                print(f'+++++++++++++++++{self.i}走+++++++++++++++++++++++')
                self.chuli_response(response)
                print(f'+++++++++++++++++{self.i}走+++++++++++++++++++++++')
            except:
                pass
    def chuli_response(self,response):
        obj_list = response['Data']['Posts']
        for info in obj_list:
            name = info['RecruitPostName']
            add = info['LocationName']
            zz = info['Responsibility'].replace('\n', '').replace('\r', '')
            PostURL = info['PostURL']
            job = f'{name}{add}{zz}{PostURL}' + '\n'
            with lock:
                with open('腾讯招聘生产消费者.txt', 'a', encoding='utf-8') as fp:
                    fp.write(job)



lock=threading.Lock()
c_queue = Queue()
flag = False
if __name__ == '__main__':
    p_queue = Queue()

    for i in range(1,11):
        p_queue.put(i)

    p_name=['p1','p2','p3']
    c_name=['c1','c2','c3']

    p_tread=[]
    c_tread=[]

    for i in p_name:
        p_s=Product(i,p_queue)
        p_s.start()
        p_tread.append(p_s)

    for i in c_name:
        c_x=Consumer(i)
        c_x.start()
        c_tread.append(c_x)

    for i in p_tread:
        i.join()

    flag=True