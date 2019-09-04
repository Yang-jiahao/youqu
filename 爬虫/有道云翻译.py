import requests
from lxml import etree
import time,json
import hashlib
import random

def jiami(sgin):
    md5=hashlib.md5()
    md5.update(bytes(sgin,encoding=('utf-8')))
    return md5.hexdigest()

def youdao(word):
    # pro = [
    #     '115.53.38.53:9999',
    #     '163.204.243.125:9999',
    #     '120.83.105.108:9999',
    #     '123.101.237.103:808',
    #     '117.28.97.217:9999',
    #     '163.204.242.200:9999',
    #     '163.204.242.118:9999',
    #     '113.124.95.69:9999'
    # ]

    salt=int(time.time()*10000)
    ts=int(time.time()*1000)
    tx="fanyideskweb" + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sgin=jiami(tx)
    """headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '244',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=173318041@221.219.233.45; OUTFOX_SEARCH_USER_ID_NCOO=1248637866.0347495; P_INFO=m13906445972_1@163.com|1565836787|0|other|00&99|bej&1564642265&other#bej&null#10#0#0|139972&1|youdaodict_client&note_client|13906445972@163.com; _ga=GA1.2.1915306413.1565859951; JSESSIONID=aaaz0iInb7uNiak6vElZw; ___rl__test__cookies=1566798184851',
    'Host': 'fanyi.youdao.com',
    'Origin': 'http://fanyi.youdao.com',
    'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }"""
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data={
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': sgin,
        'ts': str(ts),
        'bv': '6463522ba46bac94c96fd37965fadc8d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate',##最好注掉该行，不让返回压缩文件
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '236',  ##给出内容长度
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1871350561@111.193.85.119; OUTFOX_SEARCH_USER_ID_NCOO=1950439105.809919; __guid=204659719.1570426072752288800.1561001741129.7214; _ntes_nnid=f843c1d54778be721b6e22ff831fb9ed,1561001842261; P_INFO=m13353581735@163.com|1562243310|0|other|00&99|bej&1562238054&other#bej&null#10#0#0|133735&1|urs|13353581735@163.com; _ga=GA1.2.571841777.1563363133; JSESSIONID=aaaVLW6Il_ziEcphFDlZw; monitor_count=7; ___rl__test__cookies=1566782439134',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    response = requests.post(url=url,headers=headers,data=data).content.decode('utf-8')
    # response = requests.post(url=url,headers=headers,data=data,proxies={'http':random.choice(pro)}).content.decode('utf-8')
    # print(response)
    tran=json.loads(response)
    print(tran)
    jieshi=tran['smartResult']['entries']
    hello=word
    try:
        for x in jieshi:
            hello+=x.strip()
        print(hello)
    except:
        pass


if __name__ == '__main__':
    trans=input('翻译啥')
    youdao(trans)
    # print(time.time())
    # print(jiami('123'))

