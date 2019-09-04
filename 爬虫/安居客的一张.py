import requests
import os
from lxml import etree
qianxinan = open('安居客/安居客_city/黔西南.html','r',encoding='utf-8')
hahaha = etree.HTML(qianxinan.read())
xiaoqu =hahaha.xpath('//ul[@class="com-rec clearfix com-rec-w"]//dt/text()')
jiage =hahaha.xpath('//ul[@class="com-rec clearfix com-rec-w"]//dd/span/text()')

pingfang =hahaha.xpath('//ul[@class="com-rec clearfix com-rec-w"]//dd/em/text()')
print(xiaoqu)
print(jiage)
print(pingfang)
print(zip(xiaoqu,jiage,pingfang))
