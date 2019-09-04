import threading
import requests
from queue import Queue
import time

class Product(threading.Thread):
    def __init__(self, i, page_queue):
        #1.继承父类init:
        super().__init__()
        self.i = i
        self.page_queue = page_queue

       ##2.覆写run方法：
    def run(self):
        ##线程不能只干一个任务就退出，需要不断取任务：
        while True:
            ##任务停止条件：当任务队列为空的时候，线程退出
            if self.page_queue.empty():
                # print(f'===========任务耗时{end_time-start_time}==========')
                break
            q = self.page_queue.get()
            print(f'======{self.i}执行任务{q}===')

            url = f'https://careers.tencent.com/tencentcareer/api/post/Query?keyword=python&pageIndex={q}&pageSize=10'
            self.get_html(url)
            print(f'======{self.i}任务完成{q}===')


    #一、请求
    def get_html(self, url):
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        response = requests.get(url=url, headers=header).json()
        response_q.put(response)



class Consumer(threading.Thread):
    def __init__(self, j):
        #1.继承父类init:
        super().__init__()
        self.j= j

       ##2.覆写run方法：
    def run(self):
        ##线程不能只干一个任务就退出，需要不断取任务：
        while True:
            ##任务停止条件：当任务队列为空的时候，且生产者线程退出；
            if response_q.empty() and flag:
                break
            response = response_q.get()
            print(f'======{self.j}执行任务===')

            self.parse_html(response)
            print(f'======{self.j}任务完成===')

    # 二、解析函数：
    def parse_html(self, response):
        job_list = response['Data']['Posts']
        for job in job_list:
            # 工作名称：
            name = job['RecruitPostName']
            # 工作地点：
            address = job['LocationName']
            # 岗位职责：
            Responsibility = job['Responsibility']
            Responsibility = Responsibility.replace('\n', '').replace('\r', '')
            # 详情url：
            PostURL = job['PostURL']
            infor = f'工作名称:{name},工作地点：{address},岗位职责：{Responsibility},详情url：{PostURL}'
            with open('腾讯招聘.txt', 'a', encoding='utf-8')as fp:
                fp.write(infor + '\n')



response_q = Queue()##消费者队列
flag = False #标志生产者线程是否全部都死了
if __name__ == '__main__':
    start_time = time.time()
    print(start_time)

   ##1.创建生产者队列：
    page_queue = Queue()
    for i in range(1,11):
        page_queue.put(i)

   ##2.起线程，完成任务；
    product_name = ['p1', 'p2', 'p3']
    consumer_name = ['c1', 'c2', 'c3']

    p_tread = []
    c_tread = []
    for i in product_name:
        p_crawl = Product(i, page_queue)
        p_crawl.start()
        p_tread.append(p_crawl)

    for j in consumer_name:
        c_crawl = Consumer(j)
        c_crawl.start()
        c_tread.append(c_crawl)

    ##生产者阻塞主线程：
    for treadi in p_tread:
        treadi.join()

    flag = True

    end_time = time.time()
    print(end_time)
    # print(f'===========任务耗时{end_time-start_time}==========')


##1.只能起三个线程完成10页请求：
##2.同时写入到一个文件中；
