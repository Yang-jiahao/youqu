from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from lxml import etree

driver = webdriver.PhantomJS(executable_path=r'E:\爬虫\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'http://fanyi.youdao.com/'
driver.get(url=url)
# driver.find_element_by_id('inputOriginal').send_keys('Tom')
while True:
    word = input('shuru')
    driver.find_element_by_id('inputOriginal').send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id('inputOriginal').send_keys(Keys.BACK_SPACE)
    driver.find_element_by_id('inputOriginal').send_keys(word)
    driver.save_screenshot('%s.png'%word)
# driver.find_element_by_id('transMachine').click()
# time.sleep(5)
# driver.save_screenshot('有道翻译hello world.png')
# response = driver.page_source
# with open('无界面有道.html','w',encoding='utf-8') as fp:
#     fp.write(response)
# print(response)
# hello = etree.HTML(response)
# hy=hello.xpath('//div[@id="transTarget"]/p/span/text()')

# print(hy)