import json
import requests
import random
import smtplib
from email.mime.text import MIMEText
from lxml import etree
from fake_useragent import UserAgent

def reques_html(url,headers):
    response = requests.get(url=url,headers=headers).content.decode('utf-8')
    tree = etree.HTML(response)
    article_list=tree.xpath('//div[@class="new-post"]/article')
    for article in article_list:
        href=article.xpath('//h2/a/@href')
        h=random.choice(href)
        response = requests.get(url=h,headers=headers).content.decode('utf-8')
        tree = etree.HTML(response)
        article = tree.xpath('//div[@class="art-content"]/p//text()')
        name = tree.xpath('//h1/text()')[2]
        article_str = '\n'.join(article).strip()
        return article_str, name

def send_email(name,content):
    sendman='1307128051@qq.com'
    password_sqm='sbeeobhozxasiibb'
    receiver='13906445972@163.com'
    subject=name
    msg=MIMEText(content,'plain','utf-8')
    msg['Subject']=subject
    msg['TO']=receiver
    msg['From']=sendman
    try:
        smtp=smtplib.SMTP()
        print(1)
        smtp.connect('smtp.qq.com')
        print(2)
        smtp.login(sendman,password_sqm)
        print(3)
        smtp.sendmail(sendman,msg['TO'],msg.as_string())
        print(4)
        print('发送成功')
    except:
        print('失败')

if __name__ == '__main__':
    url='https://www.yuyangushi.com/yy/yisuo/'
    headers={'User-Agent':UserAgent().random}
    content,name=reques_html(url,headers)
    send_email(name,content)
