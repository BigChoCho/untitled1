# -*- coding: utf-8 -*-
import os
import random
import time
from urllib import request

from  spider_re_118.items import SpiderRe118Item
import scrapy
from spider_re_118.settings import headers
from pprint import pprint
class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['sz.lianjia.com']
    # start_urls = ['http://lianjia.com/']
    def start_requests(self):


        for page in range(1,2):
            url='https://sz.lianjia.com/zufang/pg{}'.format(page)
            print('發送頁面',url)
            #dont_filter 防止網址過濾
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True,headers=headers)
    def parse(self, response):
        infos=response.xpath('//div[@class="content__list--item"]')
        for info in infos:
            title=info.xpath('./div/p/a/text()').extract()[0].strip()
            title=title.replace(" ",",")
            href=info.xpath('./div/p/a/@href').extract()[0]
            href = 'https://sz.lianjia.com'+href
            position = info.xpath('./div/p[2]/a/text()').extract()
            position='-'.join(position)
            # print(position)
            yield  scrapy.Request(url=href,callback=self.detail_parse,dont_filter=True,headers=headers,meta={'title':title,'href':href,'position':position})
    #獲取詳情頁面
    def detail_parse(self,response):
        item =SpiderRe118Item()
        time.sleep(random.choice([2,1.5,1.2,0.5]))
        infos=response.xpath('//div[@class="content clear w1150"]')
        print("詳情網址",response.url)
        for info in infos:
            num=info.xpath('./div/i[2]/text()').extract()
            num = num[0].split('：')[-1]

            price =info.xpath('./div[3]/p/span/text()').extract()
            price=price[0]+"元/月"
            broker =info.xpath('./div[3]/ul[2]/li/div/span/@title').extract()[0]
            styles = info.xpath('.//p[@class="content__article__table"]//span/text()').extract()
            style = styles[0]
            ting = styles[1]
            size = styles[2]
            direction = styles[3]
            img=r'C:\Users\a3858\PycharmProjects\untitled1\py-re-62\spider_re_118\img\\'+response.meta['title']
            # print(num,price,broker,style,ting,size,direction)

            item['title']=response.meta['title']
            item['href'] =response.meta['href']
            item['position'] =response.meta['position']
            item['num'] =num
            item['price'] =price
            item['broker'] =broker
            item['style'] =style
            item['ting'] =ting
            item['size'] =size
            item['direction'] =direction
            yield item
            srcs = info.xpath('.//div[@class="content__article__slide__item"]/img/@src').extract()
            #下載圖片
            if srcs!=0:
                for src in srcs :
                    img_name = str(time.time())+'.jpg'
                    if not os.path.exists(img):
                        #沒有就創建
                        os.makedirs(img)
                        #下載對象的名子,跟路徑
                    request.urlretrieve(src,img+"\\"+img_name)