import re
import requests
url = 'https://maoyan.com/board'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url,headers).text
# print(response)

dd = re.compile(r'<dd>(.*?)</dd>',re.S)
dd_list = dd.findall(response)#[['1'],['name']]
# print(type(dd_list))
print(dd_list[0])
for i in dd_list:
    # print(i)
    # 排名
    rank_rule = re.compile(r'<i class="board-index board-index-(.*?)">')
    rank = rank_rule.findall(i)[0]#['1']


    # 电影名
    name_rule = re.compile(r'<p class="name">.*?>(.*?)</a></p>')
    name = name_rule.findall(i)[0]


    # 主演
    actor_rule = re.compile(r'主演：(.*?)\n')
    actor = actor_rule.findall(i)[0]

    # 上映时间
    releasetime_rule = re.compile(r'<p class="releasetime">上映时间：(.*?)</p>')
    times = releasetime_rule.findall(i)[0]

    # 评分
    score_rule = re.compile(r'<i class="integer">(.*?)</i><i class="fraction">(.*?)</i>')
    scores = score_rule.findall(i)[0]
    score = score_rule.findall(i)[0][0]+score_rule.findall(i)[0][1]

    maoyan = "{}，{}，{},{}，评分{}\n".format(rank,name,actor,times,score)
    with open('猫眼电影.txt','a',encoding='utf-8') as fp:
        fp.write(maoyan)