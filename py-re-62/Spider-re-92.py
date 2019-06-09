import pymongo
client = pymongo.MongoClient()
#spider是數據庫
db = client.spider_92
#集合庫
std = db.profile
#獲取數據
datas = std.find()
#遍歷返回字典值
for data in datas:
    print(data['singer'])