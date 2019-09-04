import re
import requests
import json
url = 'https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5732cb185bc149bcb51004b440171101'
headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url,headers).text
# pattern = re.compile(r'"http.*?"')
pattern =re.compile(r'<a t.*?</a>')
result = pattern.findall(response)
print(len(result))
json.dump()