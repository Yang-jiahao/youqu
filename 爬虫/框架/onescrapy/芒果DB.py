import pymongo

# 连接客户端
client=pymongo.MongoClient("localhost")

# 建库
db=client['test0506']

# 建表，集合
collections=db['users']

# # 插入数据
# collections.insert({"name":'pxt',"age":18})
# collections.insert({"name":'song',"age":28})
#
# user1={"name":"lm","age":21}
# user2={"name":"wtt","age":22}
# user3={"name":"lys","age":23}
#
# # 一次性插入多条数据
# collections.insert_many([user1,user2,user3])

# 查找数据
user=collections.find({'age':18})

print(user)

for i in user:
    print(i)

cha=collections.find({'age':{"$gt":18}})
