import re
douyin=open(r'D:\Fiddler\抖音\ndroid&iid=8.json','r',encoding='utf-8')
qingiu=douyin.read()
print(qingiu)
# re.compile('"aweme_list":(.*?)"height":720')