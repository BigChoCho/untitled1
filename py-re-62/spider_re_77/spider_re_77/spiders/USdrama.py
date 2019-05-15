import scrapy

from spider_re_77.items import USdramaItem

class USdrama(scrapy.Spider):
    name = "usdrama"
    #yahoo電影
    start_urls = ['https://movies.yahoo.com.tw/movie_intheaters.html?guccounter=1']

    def parse(self, response):
            '''
                默认已经得到了网页
                反馈的内容用response表示
                其中包含需要的 所有数据
                :param response:
                :return:
                '''

            # movies = response.xpath('//div[@class="recruit-wrap recruit-margin"]/div')
            # print(movies)

           #通过下面xpath，能够找到所有电影
            #重ul該類中獲取所有li
            movies = response.xpath('//ul[@class="release_list"]/li')
            print("操操")
            print("Moives len: {0}".format(len(movies)))
            for movie in movies:
                '''
                每个movie都需要转换成一个item
                需要先生成一个Item实例对象

                '''
                #extract提取所有屬性
                #在items裡的函數
                item = USdramaItem()
                item['name'] = movie.xpath('./div/a/@data-ga').extract()[0]
                item['href'] = movie.xpath('./div/a/@href').extract()[0]
                # tv属性很可能有问题
                tv = movie.xpath('.div/a/img/@src')
                print(tv)
                if len(tv):
                    item['tv'] = tv.extract()[0]
                else:
                    item['tv'] = ""

                print('Item.name: {0}'.format(item['name']))
                print('Item.href: {0}'.format(item['href']))
                print('Item.tv: {0}'.format(item['tv']))


                # item只能通过yield返回(因為是疊代)
                yield item