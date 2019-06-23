# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from spider_re_116.items import SpiderRe116Item
from spider_re_116.mysqlpipelines.sql import Sql
class SpiderRe116Pipeline(object):
    def process_item(self, item, spider):
        print('process_item啟用中')
        #判斷類型是否相同
        if isinstance(item,SpiderRe116Item):
            ipaddress=item['ipaddress']
            ret=Sql.selct_name(ipaddress)
            if ret[0] ==1:
                print('已存在')
            else:
                country = item['country']
                ipaddress = item['ipaddress']
                port = item['port']
                serveraddr = item['serveraddr']
                isanonymous = item['isanonymous']
                type = item['type']
                alivetime = item['alivetime']
                verifictiontime = item['verifictiontime']
                Sql.insert(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime)
                print('儲存:',country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime)
