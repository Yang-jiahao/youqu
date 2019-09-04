import requests
url='http://api.tianxianle.com/jx/dapi.php?id=o6t1naKhqaajl2lskZRtZWQO0O0O'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).content
# print(response)
with open('战争之王.avi','wb')as f:
    f.write(response)
