import requests
#
# url = 'https://www.baidu.com/s?wd=宋亚娇'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
#
# response = requests.get(url=url,headers=headers).content.decode('utf-8')
#
# with open('syj.html','w',encoding='utf-8') as fp:
#     fp.write(response)
def sousuo(kwords):
    url = 'https://www.baidu.com/s?'
    params = {"wd":kwords}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    response = requests.get(url=url,params=params,headers=headers).content.decode('utf-8')
    with open('%s.html'%kwords,'w',encoding='utf-8') as fp:
        fp.write(response)

if __name__ == '__main__':
    kwords = input('搜啥')
    sousuo(kwords)