# 使用session
import requests
sess = requests.session()
def login(sess):#登陆
    url = 'http://www.renren.com/PLogin.do'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    #     "Cookie":''
    }
    data = {
        'email':'13906445972',
        'password':'duoyansanwei'
    }
    response = sess.post(url,data,headers).text
    with open('login.html','w',encoding='utf-8') as fp:
        fp.write(response)
    setting_url = 'http://www.renren.com/971983695'
    setting_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    setting_response = sess.get(url=setting_url,headers=setting_headers).text
    with open('dengluhou.html','w',encoding='utf-8') as f:
        f.write(setting_response)
login(sess)