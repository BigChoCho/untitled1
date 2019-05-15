# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SpiderRe77Pipeline(object):
    def process_item(self, item, spider):
        return item
class USdramaPipeline(object):
    '''
     此方法必须被实现
     用来具体处理item内容
     且必须返回一个item
     '''

    def __init__(self):
        print("init ... yahoo.json")
        #創建
        self.file = open('yahoo.json', 'wb')

    def process_item(self, item, spider):
        '''
        此案例只是把item值打印出来
        :param item:
        :param spider:
        :return:
        '''
        print(item['name'])
        with open('yahoo.json', 'a') as f:
            #轉換字典格式
            json.dump(dict(item), f)

        return item
