# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SpiderRe113Pipeline(object):
    def process_item(self, item, spider):
        return item
class MeijuttPipeline(object):
        def __init__(self):
            self.file = open('meiju.json','w',encoding='utf-8')
        def process_item(self,item,spider):

            json.dump(dict(item),open('meiju.json','a',encoding='utf-8'),ensure_ascii=False)
            return item
        def close_spider(self,spider):
            self.file.close()
            print('關閉')