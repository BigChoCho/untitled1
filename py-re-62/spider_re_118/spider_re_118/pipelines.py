# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from openpyxl import Workbook

class SpiderRe118Pipeline(object):
    def __init__(self):
        self.file= open('lianjia.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        str= json.dumps(dict(item),ensure_ascii=False)
        str=str+'\n'
        self.file.write(str)
        print('仔入文件',item['title'],
        item['href'],
        item['position'],
        item['num'],
        item['price'],
        item['broker'],
        item['style'],
        item['ting'],
        item['size'] ,
        item['direction'])
        return item
    def close_spider(self,spider):
        self.file.close()
        #創建excel
class lianPipeline(object):
    def __init__(self):
        self.wb=Workbook()
        self.ws= self.wb.active
        self.ws.append(['title',
        'href',
        'position',
        'num',
        'price',
        'broker',
        'style',
        'ting',
        'size',
        'direction'])
    def process_item(self, item, spider):

        print('載入excel', item['title'],
              item['href'],
              item['position'],
              item['num'],
              item['price'],
              item['broker'],
              item['style'],
              item['ting'],
              item['size'],
              item['direction'])
        line=[item['title'],
        item['href'],
        item['position'],
        item['num'],
        item['price'],
        item['broker'],
        item['style'],
        item['ting'],
        item['size'] ,
        item['direction']]
        self.ws.append(line)
        self.wb.save('lianjia.xlsx')
        return item