# -*- coding: utf-8 -*-
import scrapy
from spider_re_117.items import SpiderRe117Item
class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/archives/57.html']

    def parse(self, response):
        item = SpiderRe117Item()
        imgurls = response.css('.post img::attr(src)').extract()
        print(imgurls)
        item['imgurl']=imgurls

        yield item