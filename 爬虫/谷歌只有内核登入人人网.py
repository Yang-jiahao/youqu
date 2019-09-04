import time
from lxml import etree
from selenium import webdriver

def renren():
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
    time.sleep(10)
    drivers.save_screenshot('谷歌登录人人后.png')
# 如果登录了，那就判断自己的账户昵称是否存在了嘛
if __name__ == '__main__':
    renren()
