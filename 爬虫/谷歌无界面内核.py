import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
# 百度德玛西亚
"""
driver = webdriver.Chrome(executable_path=r'E:\爬虫\chrome\chromedriver.exe')
url = 'https://baidu.com'
driver.get(url=url)
driver.find_element_by_id('kw').send_keys('德玛西亚')
driver.find_element_by_id('su').click()
time.sleep(6)
driver.close()
"""

drivers=webdriver.Chrome(executable_path=r'E:\爬虫\chrome\chromedriver.exe')
url = 'http://www.renren.com/'
drivers.get(url=url)

drivers.find_element_by_id('email').send_keys('13906445972')
drivers.find_element_by_id('password').send_keys('duoyansanwei')
drivers.find_element_by_id('login').click()

ym = drivers.page_source
tree = etree.HTML(ym)
static = tree.xpath('//dl[@id="code"]/@style')
# 写个判断完全没有问题
if static=="display: none;":
    drivers.find_element_by_id('email').send_keys('13906445972')
    drivers.find_element_by_id('password').send_keys('duoyansanwei')
    drivers.find_element_by_id('login').click()
elif static=="display: block;":
    drivers.find_element_by_id('email').send_keys('13906445972')
    drivers.find_element_by_id('password').send_keys('duoyansanwei')
    yan=input('请输入验证码')
    drivers.find_element_by_id('icode').send_keys(yan)
    drivers.find_element_by_id('login').click()
time.sleep(4)
drivers.save_screenshot('谷歌登录人人后.png')
# 无界面登录人人网
#
"""
drivers=webdriver.PhantomJS(executable_path=r'E:\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')#这个内核不对
url = 'http://www.renren.com/'
drivers.get(url=url)
drivers.find_element_by_id('email').send_keys('13906445972')
drivers.find_element_by_id('password').send_keys('duoyansanwei')
drivers.find_element_by_id('login').click()
time.sleep(3)

print(drivers.page_source)
drivers.save_screenshot('renrenlogins.png')
"""
