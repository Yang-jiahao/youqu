import requests
import json

url = 'https://www.creditchina.gov.cn/xinyongxinxi/index.html?index=0&keyword=拜克洛克科技'
proxies={
    'http':'http://123.163.96.80:9999',
    'https':'https://182.34.36.113:9999'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }

response = requests.get(url,proxies).text
# responses = json.loads(response)
# datas = response['data']['results']
# names = []
# print(datas)
print(response)
# for i in range(len(datas)):
#     names.append(i["name"])


'''
'https://www.creditchina.gov.cn/xinyongxinxixiangqing/default.html?isEncryStr=1&encryStr=bHBReWk7RnY2cQ%3D%3D%0A&name=%E9%9D%92%E5%B2%9B%E6%8B%9C%E5%85%8B%E6%B4%9B%E5%85%8B%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&isEncryStr=1'
'https://www.creditchina.gov.cn/xinyongxinxixiangqing/default.html?isEncryStr=1&encryStr=cGJkZEEyc1tnew%3D%3D%0A&name=%E5%8C%97%E4%BA%AC%E6%8B%9C%E5%85%8B%E6%B4%9B%E5%85%8B%E7%A7%91%E6%8A%80%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&isEncryStr=1'
'''
# https://www.creditchina.gov.cn/api/credit_info_search?keyword=&templateId=&page=1&pageSize=10