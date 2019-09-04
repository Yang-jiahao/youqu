import requests
url='https://vdse.bdstatic.com//f82125351956d8043d9c5af070c5f8b2?authorization=bce-auth-v1%2Ffb297a5cc0fb434c971b8fa103e8dd7b%2F2017-05-11T09%3A02%3A31Z%2F-1%2F%2F44aee7aa66c0983b53bbf84811daa2f26a6fe596f5e27a2ea9bc631b961c89f0'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url=url,headers=headers).content
# print(response)
with open('苹果.mp4','wb')as f:
    f.write(response)
    f.close()

