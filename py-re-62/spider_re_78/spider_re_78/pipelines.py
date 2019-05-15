# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SpiderRe78Pipeline(object):
    def process_item(self, item, spider):
        return item
class QQPipeline(object):


    def __init__(self):
        print("QQPipline")
        # 創建
        self.file = open('QQ1.json', 'wb')

    def process_item(self, item, spider):
          '''
          此案例只是把item值打印出来
          :param item:
          :param spider:
          return:
          '''
          print("職稱:",item['name'])
          print("訊息:",item['positionInfo'])
          print("網址",item['name'],item['detailLink'])
          print(item['workLocation'])


          with open('QQ1.json', 'a') as f:
              #轉換字典格式
              json.dump(dict(item), f)

          return item