import requests
import json
import os
url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(url=url,headers=headers).json()
print(response)

# 判断文件存在
isExit = os.path.exists('文件夹')