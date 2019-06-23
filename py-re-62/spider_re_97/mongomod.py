from pymongo import MongoClient

class MongoAPI(object):
    def __init__(self,ip,port,database_name,table_name):
        self.ip = ip
        self.port =port
        self.database_name=database_name
        self.table_name=table_name
        self.conn= MongoClient(host=self.ip,port=self.port)
        #進入數據庫
        self.db = self.conn[self.database_name]
        #進入數據表
        self.table = self.db[self.table_name]

        #查找第一個屬性
    def get_one(self,query):
        return self.table.find_one(query,property={"_id":False})
    #所有屬性
    def get_all(self,query):
        return  self.table.find(query)
    #插入數據
    def add(self,dict):
        return self.table.insert(dict)
    #刪除數據
    def delate(self,query):
        return self.table.delete_many(query)
    def check(self,query):
        ret = self.table.find_one(query)
        #數據庫不為空的情況下返回數據
        return ret !=None
    def update(self,query,dict):
        #$set更改部分字段
        self.table.update(query,{'$set':dict},upsert=True)