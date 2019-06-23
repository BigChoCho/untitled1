# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SpiderRe79Pipeline(object):
    def process_item(self, item, spider):
        return item

class donbonPipeline(object):
    def __init__(self):
        self.file = open('donbon.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        str = json.dumps(dict(item), ensure_ascii=False)

        str = str + '\n'
        self.file.write(str)
        print("spider開啟")
        print('電影名稱: ', item['title'])
        print('電影網址: ', item['href'])
        print('電影圖片: ', item['src'])


def close_spider(self, spider):
        self.file.close()

