from urllib import request
from bs4 import BeautifulSoup
import re
#bs4將檔案直接存取在內存中,相對etree則是局部遍歷
url = "http://www.baidu.com/"

rsp = request.urlopen(url)
#返回html文件
content=rsp.read()
#使用該文件串建bu4解析器(文檔,引擎)格式也整理好了
soup = BeautifulSoup(content,'lxml')
#尋找所有關於此節點名稱
tags = soup.find_all(name = "meta")
print(tags)
print("=="*12)
#運用正則找出me相關的名稱(正則找尋節點,以該節點中巡找對應屬性及內容
tags =soup.find_all(re.compile('^me'),content="always")
for tag in tags:
    print(tag)
