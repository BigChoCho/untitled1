from urllib import request
from bs4 import BeautifulSoup
#bs4將檔案直接存取在內存中,相對etree則是局部遍歷
url = "http://www.baidu.com/"

rsp = request.urlopen(url)
#返回html文件
content=rsp.read()
#使用該文件串建bu4解析器(文檔,引擎)格式也整理好了
soup = BeautifulSoup(content,'lxml')
#自動轉碼,
content= soup.prettify()
print(content)
print("=我是基德1="*5)
#打印出html中的<head>內容
print(soup.head)
print("=我是基德2="*5)
#<meta>內容(1組)
print(soup.meta)
print("=我是基德3="*5)
#尋找節點
print(soup.link)
#節點名稱
print(soup.link.name)
print("=我是基德4="*5)
#節點的所有屬性
print(soup.link.attrs)
print("=我是基德5="*5)
#改變屬型值(因為是在內存裡,所以可以直接進行修改)
soup.link.attrs["type"] = "CHANGEOVER"
print(soup.link)
print("=我是基德6="*5)
#所有
print(soup.title)
#名子
print(soup.title.name)
#屬性
print(soup.title.attrs)
#內容
print(soup.title.string)
