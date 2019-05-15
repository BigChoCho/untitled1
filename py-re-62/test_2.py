import scrapy
from spider_re_78.items import QQItem
import time
import json


class qqscray(scrapy.Spider):
    name = "qqspider"

    allowed_domains = ['hr.tencent.com']
    #獲取XHR的Response的url
    start_urls = [
        'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557895020042&countryId=1&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=us'
    ]

    def parse(self, response):
        # decode=解碼encode=編碼,json.loads轉成字典類型
        dicts = json.loads(response.body.decode().encode('utf-8'))
        # 查找該字典對應值
        dicts = dicts['Data']
        # 此key對應的是list類型的值
        dicts = dicts['Posts']

        for href in dicts:
            item = QQItem()
            detailLink="https://careers.tencent.com/jobdesc.html?postId="+href['PostId']
            name = href["RecruitPostName"]
            positionInfo=href["Responsibility"]
            workLocation ="地點:"+href["CountryName"]+",類型:"+href['LocationName']+",發布日期:"+href["LastUpdateTime"]

            item['name'] = name
            item["detailLink"] = detailLink
            item['positionInfo'] = positionInfo
            item['workLocation'] = workLocation

            yield item