import scrapy
import re
from spider_re_78.items import QQItem
from selenium import webdriver
import time
from lxml import etree
import json

class qqscray(scrapy.Spider):
    name = "qqspider"
    # 设置只能爬去腾讯域名的信息
    allowed_domains = ['hr.tencent.com']
    #獲取XHR的Response的url
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557895020042&countryId=1&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=us'
    ]
    def parse(self, response):
        time.sleep(20)
        print("為何沒咚咚")
        #decode=解碼encode=編碼,json.loads轉成字典類型
        dicts=json.loads(response.body.decode().encode('utf-8'))
        #查找該字典對應值
        dicts=dicts['Data']
        #此key對應的是list類型的值
        dicts=dicts['Posts']
        print("時間搓",time.time())

        print("_________________"*5)
        #藉由無頭瀏覽器獲取動態js
        # driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
        # driver.get('https://careers.tencent.com/search.html?query=co_1&sc=1')
        # time.sleep(10)
        # #等待3秒
        # driver.implicitly_wait(3)
        # tree = etree.HTML(driver.page_source)
        # etree.tostring(tree)
        #
        # tress = tree.xpath('//div[@class="recruit-wrap recruit-margin"]/div')
        for href in dicts:
            item = QQItem()
            detailLink="https://careers.tencent.com/jobdesc.html?postId="+href['PostId']
            name = href["RecruitPostName"]
            positionInfo=href["Responsibility"]
            workLocation ="地點:"+href["CountryName"]+",類型:"+href['LocationName']+",發布日期:"+href["LastUpdateTime"]
            # name=names.xpath('./a/h4[@class="recruit-title"]/text()')
            # positionInfo=names.xpath('./a/p[@class="recruit-text"]/text()')
            # workLocations = names.xpath('./a/p[@class="recruit-tips"]/span/text()')
            # workLocation=workLocations[0],",地點:"+workLocations[1],",類型:"+workLocations[2],",發布日期:"+workLocations[3]


            # item['name'] = name[0]
            item['name']=name
            item["detailLink"]=detailLink
            item['positionInfo']=positionInfo
            item['workLocation']=workLocation

            # 处理继续爬去的链接
            # 通过得到当前页，提取数字，把数字加1，替换原来的数字，就是下一个页面地址
            # 提取当前也的数字

            curpage = re.findall('(\d+)', response.url)
            curpage = curpage[2]
            # 生成下一页url
            page = int(curpage) + 1
            url = response.url.replace("Index=1", "Index=" + str(page))
            print(url)

            # 把地址通过yield返回
            # 注意callback的写法
            #處理完再調用parse函數,並且把url回傳response


            yield item
        yield scrapy.Request(url, callback=self.parse)






