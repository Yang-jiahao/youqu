import requests
"""
i=1
for d in range(10):
    x = d*50
    ss = str(int(x))
    url = 'http://tieba.baidu.com/f?kw=还珠格格&ie=utf-8&pn=%s'%ss
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    with open('%d.html' % i, 'w', encoding='utf-8') as  fp:
        fp.write(response)
    i+=1
"""

"""
# 优化
def tieba(name):
    i=0
    while True:
        url = f'http://tieba.baidu.com/f?kw={name}&ie=utf-8&pn={i*50}'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url=url,headers=headers).content.decode('utf-8')
        if 'class="last pagination-item "' in response:
            with open('第%s页.html'%(1+i),'w',encoding='utf-8') as fp:
                fp.write(response)
        else:
            with open('第%s页.html'%(1+i),'w',encoding='utf-8') as fp:
                fp.write(response)
            break
        i+=1
if __name__=='__main__':
    name = input('搜啥啊')
    tieba(name)
  
"""

# 股吧,有问题
'''
def guba_zhannei(baname,kname):
    i = 1
    while True:
        url = 'http://tieba.baidu.com/f/search/res?ie=utf-8&kw=%s&qw=%s&pn=%d'%(baname,kname,i)
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url=url, headers=headers).content.decode('utf-8')
        if 'class="last"' in response and i<4:
            with open('%s第%d页.html'%(baname,i),'w',encoding='utf-8') as fp:
                fp.write(response)
        else:
            with open('%s第%d页.html'%(baname,i),'w',encoding='utf-8') as fp:
                fp.write(response)
            break
        i+=1

if __name__=='__main__':
    baname = input('吧名')
    kname = input('吧内搜索')
    guba_zhannei(baname,kname)
'''

# 东方财富
"""
def dfcf(name):
    i=1
    while True:
        url = f'http://so.eastmoney.com/web/s?keyword={name}&pageindex={i}'
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
        response = requests.get(url=url,headers=headers).content.decode('utf-8')
        if '下一页' in response and i < 4:
            with open('%s第%d页.html'%(name,i),'w',encoding='utf-8') as fp:
                fp.write(response)
        else:
            with open('%s第%d页.html' % (name,i), 'w', encoding='utf-8') as fp:
                fp.write(response)
            break
        i+=1
name = input('搜啥')
dfcf(name)
"""
# 股吧,ok
"""
for i in range(10):
    url = 'http://guba.eastmoney.com/list,000006_%d.html'%i
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url,headers=headers).content.decode('utf-8')
    with open('guba%d.html'%i,'w',encoding='utf-8') as fp:
        fp.write(response)
"""

# 高德地图
import json,re
url = 'https://www.amap.com/service/cityList?version=201981914'
header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
responsejson = requests.get(url=url,headers=header).json()

city_json = responsejson['data']['cityByLetter']
li = [chr(i) for i in range(ord('A'),ord('Z')+1)]
citys = []
for i in li:
    if i in city_json:
        city_jsons = responsejson['data']['cityByLetter'][i]
        for i in city_jsons:
            citys.append(i)
    else:
        continue
for i in citys:
    print(i['name'],i['adcode'])
    try:
        url = f'https://www.amap.com/service/weather?adcode={i["adcode"]}'
        responses = requests.get(url=url,headers=header).text
        city_weathers = json.loads(responses)
        city_weather = city_weathers['data']['data']
        city_weather_one = city_weather[1]
        city_weather_one_list = city_weather_one['forecast_data']
        city_write = city_weather_one_list[1]
        weather = f"{i['name']}今天{city_write['weather_name']},最高温度{city_write['max_temp']},最低温度{city_write['min_temp']},{city_write['wind_direction_desc']},风力{city_write['wind_power_desc']}"

        with open('quanguotianqi.txt','a',encoding="utf-8") as fp:
            fp.write(weather+'\n')
    except:
        pass



# for key,value in city_json:
#     print(value)
# print(city_json)

# with open('gaodect.txt','r',encoding='utf-8') as fp:
#     str = fp.read()
#     for i in str:
#         print(i)