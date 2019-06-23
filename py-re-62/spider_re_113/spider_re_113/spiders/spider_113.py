# -*- coding: utf-8 -*-

import scrapy
from spider_re_113.items import MeijuttItem
from lxml import etree
class Spider113Spider(scrapy.Spider):
    name = 'spider_113'
    #允許域名
    allowed_domains = ['meijutt.com']
    #起始地址
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        print('啟用')
        content = etree.HTML(response.body.decode('GBK'))
        movis=content.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movi in movis:
            name = movi.xpath('./h5/a/text()')[0]
            state= movi.xpath('./span[@class="state1 new100state1"]/font/text()')[0]
            print(name,state)
            item=MeijuttItem()
            item['name']=name
            item['state']=state

            yield item