import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree

def douyu(url):
    count = 1
    driver = webdriver.PhantomJS(executable_path=r'E:\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get(url=url)
    a = []
    while True:
        page = driver.page_source
        time.sleep(10)
        trees = etree.HTML(page)
        li_list = trees.xpath('//div[@class="layout-Module-container layout-Cover ListContent"]/ul[@class="layout-Cover-list"]/li')
        print(len(li_list))
        for li in li_list:
            types = li.xpath('.//span[@class="DyListCover-zone"]/text()')[0]
            title = li.xpath('.//h3[@class="DyListCover-intro"]/text()')[0]
            hot = li.xpath('//span[@class="DyListCover-hot"]//text()')
            name = li.xpath('//h2[@class="DyListCover-user"]//text()[last()]')
            dic = {}
            dic['type'] = types
            dic['title'] = title
            dic['hot'] = hot
            dic['name'] = name
            a.append(dic)
            print(types,title,hot,name)
        xiayiye  = trees.xpath('//li[@class=" dy-Pagination-next"]/@aria-disabled')
        if xiayiye=='"false"':
            driver.find_element_by_class_name('" dy-Pagination-next"').click()
            count+=1
        else:
            break
        print(count)
    # with open('斗鱼.json', 'w', encoding='utf-8') as fp:
    #     json.dump(a, fp, ensure_ascii=False)

if __name__ == '__main__':
    url='https://www.douyu.com/directory/all'
    douyu(url=url)
