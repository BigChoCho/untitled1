'''
爬去丑事百科， 页面自己来找
分析：
1. 需要用到requests爬去页面，用xpath、re来提取数字
2. 可提取信息谁用户头像链接，段子内容，点赞，好评次数
3. 保存到json文件中

大致分三部分
1. down下页面
2。 利用xpath提取信息
3. 保存文件落地
'''

import requests
from lxml import etree
import re
url = "https://www.qiushibaike.com/article/120535270"
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Language":"en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36/iZg0L8NK-43"

}
rsp =requests.get(url,headers=headers)

#返回文本類型
html = rsp.text
# print(html)
#解析成html文件
html = etree.HTML(html)
# print(html)
#尋找div含有id的屬性跟其對應值contains表示包含div到id中間的任一字串
rst = html.xpath('//div[contains(@id, "qiushi_tag")]')
for r in rst:
    print("所有包含",r.text)
    item = {}
    print("啥鬼阿",r)

    content = r.xpath('//div[@class="content"]//text()')
    print(content)
    for i in content:
        print(i)