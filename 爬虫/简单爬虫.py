import requests

# 1.确定请求的网站
url = "https://www.baidu.com/"
# 2.加上伪装headers
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

# 3.请求页面
response = requests.get(url=url,headers=headers)

print(response)
print(response.text)

# 4.使用字节流不乱码的方式
response = response.content.decode('utf-8')

# 5.保存页面
with open('baidu-headers.html','w',encoding='utf-8') as fp:
    fp.write(response)