import scrapy
from urllib import  request

from spider_re_79.items import IonlineItem

class DorbonSpider(scrapy.Spider):

    name = 'dorbon'
    allowed_domains = ['movie.douban.com']

    start_urls = ['https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=']

    def parse(self, response):
        print("啟動中")
        movieall = response.xpath('//div[@class="movie-info"]')
        for movie in movieall:
            title=movie.xpath('./div/span[@class="movie-name-text"]/a/text()').extract()[0]
            href=movie.xpath('./div/span[@class="movie-name-text"]/a/@href').extract()[0]
            src = movie.xpath('preceding-sibling::*[1]')
            src=src.xpath('./img[@class="movie-img"]/@src').extract()


            item=IonlineItem()
            item['title'] = title
            item['href'] = href
            if len(src):
                item['src'] = src
            else:
                item['src'] = "沒有搜到"
            yield item



