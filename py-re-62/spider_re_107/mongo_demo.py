
__author__="SadClown"
import pymongo
from pprint import pprint
class MongoMod(object):
    def __init__(self,ip,port,database,table):
        self.client = pymongo.MongoClient(ip,port)
        #創建庫,或使用
        self.db=self.client[database]
        #創表或使用
        self.collection = self.db[table]
        print('吊起')
    def to_mongodb(self,data):
        try:
            self.collection.insert(data)
        except Exception as f:
            pprint('插入失敗',f)