'''
'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'
'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20'
# 一张20

'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1'
'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=1&limit=1'
# 一张1
'''
import requests
import json

for i in range(100):
    url = f'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={i}&limit=1'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url,headers=headers).content.decode('utf-8')
    movie = json.loads(response)
    rank = movie[0]['rank']#排名
    score = movie[0]['score']#评分
    image = movie[0]['cover_url']#海报
    types = movie[0]['types'][0]#类型
    regions = movie[0]['regions'][0]#地区
    title = movie[0]['title']#电影名
    release_date = movie[0]['release_date']#上映时间
    actors = movie[0]['actors']#演员
    shuoming = f'第{rank}名,{title},{release_date}{regions}上映,豆瓣评分{score},类型{types},{actors}'+'\n'
    with open('doubanyingping.txt','a',encoding='utf-8') as fp:
        fp.write(shuoming)
# print(movies_name)
