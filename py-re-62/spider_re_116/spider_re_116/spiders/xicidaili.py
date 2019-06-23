# -*- coding: utf-8 -*-
import scrapy
from spider_re_116.items import SpiderRe116Item
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/']
    def parse(self, response):
        item_1=response.xpath('//tr[@class="odd"]')
        item_2 = response.xpath('//tr[@class=""]')
        items = item_1+item_2
        infos = SpiderRe116Item()

        for item in items:
            country= item.xpath('./td/img/@alt').extract()
            if country != []:
                country=country[0]
            else:
                country='空'
            ipaddress =item.xpath('./td[2]/text()').extract()[0]
            port=item.xpath('./td[3]/text()').extract()[0]
            serveraddr=item.xpath('./td[4]/text()').extract()
            try:
                serveraddr = serveraddr[0]
            except:
                serveraddr = '空'
            isanonymous=item.xpath('./td[5]/text()').extract()[0]
            type=item.xpath('./td[6]/text()').extract()[0]
            alivetime=item.xpath('./td[7]/text()').extract()[0]

            verifictiontime=item.xpath('./td[8]/text()').extract()
            try:
                verifictiontime = verifictiontime[0]
            except:
                verifictiontime = '空'
            # print(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,varifictiontime)
            print('??',verifictiontime)
            infos['country']=country
            infos['ipaddress']=ipaddress
            infos['port']=port
            infos['serveraddr']=serveraddr
            infos['isanonymous']=isanonymous
            infos['type']=type
            infos['alivetime']=alivetime
            infos['verifictiontime']=verifictiontime
            print('xicidaili完畢')
            yield infos