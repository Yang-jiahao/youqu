import requests

url = 'https://www.jd.com/?cu=true&utm_source=haosou-search&utm_medium=cpc&utm_campaign=t_262767352_haosousearch&utm_term=5512152820_0_f1b23256f5cc45449045ef4522a9ba3b'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

response = requests.get(url=url,headers=headers).text

with open('jd.html','w',encoding='utf-8') as fp:
    fp.write(response)
