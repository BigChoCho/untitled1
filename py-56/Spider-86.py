from urllib import request
from bs4 import BeautifulSoup
#bs4將檔案直接存取在內存中,相對etree則是局部遍歷
url = "http://www.baidu.com/"

rsp = request.urlopen(url)
#返回html文件
content=rsp.read()
#使用該文件串建bu4解析器(文檔,引擎)格式也整理好了
soup = BeautifulSoup(content,'lxml')
print(soup.name)
print("=="*12)
# .contents
# 屬性可以將
# tag的子節點以列表的形式輸出。
for nde in soup.head.contents:
    #如節果點名稱為meta打印該節點所有屬性
    if nde.name == "meta":
        print(nde)
    if nde.name == "title":
        print(nde.string)