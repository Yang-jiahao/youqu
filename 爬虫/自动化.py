import time
from selenium import webdriver

# 1.定义一个浏览器
driver = webdriver.PhantomJS(executable_path=r'E:\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 2.请求页面
url = 'https://www.baidu.com/'
driver.get(url=url)
driver.find_element_by_id('kw').send_keys('香港')
driver.find_element_by_id('su').click()
time.sleep(3)
with open('无界面.html','w',encoding='utf-8') as fp:
    fp.write(driver.page_source)
