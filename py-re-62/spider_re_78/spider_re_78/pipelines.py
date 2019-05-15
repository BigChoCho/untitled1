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

    # spider開始時觸發
    def process_item(self, item, spider):

        print("spider開啟")

         #假设数据需要写入文件
         #那么在什么时候关闭，打开文件

        print("職稱:",item['name'])
        print("訊息:",item['positionInfo'])
        print("網址",item['name'],item['detailLink'])
        print(item['workLocation'])
        #每寫入一次換行
          #将 dict(item) 对象编码成 JSON 字符串
          #json_dumps(dict)时，如果dict包含有汉字，一定加上ensure_ascii=False。否则按参数默认值
          #https://zhuanlan.zhihu.com/p/37504880(詳情)
        # content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        # f =open('QQ1.json','wb')
        # f.write(content.encode())
          # self.file.write(content)
        # print("這是啥",type(content))
        # with open('QQ1.json', 'wb') as f:
        #     f.write(content.encode())
        with open('QQ1.json', 'a') as f:
            # 轉換字典格式

            json.dump(dict(item,ensure_ascii=False), f)
            f.write('\n')


        return item
    #spider關閉時觸發
    def close_spider(self,spider):
        self.file.close()
        print("sipider關閉了")