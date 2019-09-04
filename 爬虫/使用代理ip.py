# 使用代理
import requests
url = 'https://www.jd.com/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
proxies={
    'http':'http://60.13.42.178:9999',
    'https':'https://122.193.244.125:9999'
}
# 只要可以对应上https的可以
response = requests.get(url,proxies)
# get只可以传入两个参数
print(response)

