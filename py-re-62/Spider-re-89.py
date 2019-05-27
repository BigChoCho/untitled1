

from urllib import request
import requests
import os
from lxml import etree
import random
import time

def Sch(num,size,tosize):
    #獲取百分比
    per = 100*num*size/tosize
    if per>100:
        per=100
    print('當前下載進度',per)
#音頻文件下載OR遠程數據
#(url, filename=None, reporthook=None, data=None):
#網址,數據重組路徑+文件名,回掉函數,返回一个包含两个元素的(filename, headers) 元组，filename 表示保存到本地的路径，header表示服务器的响应头

user_agent =["Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36",
             "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
             "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
]

headers = {'User-Agent':random.choice(user_agent)}
url='https://www.xvideos.com/'
response = requests.get(url,headers=headers)
html = etree.HTML(response.text)
img_url = html.xpath('//div[@class="thumb"]/a/img/@data-src')
count=0
for img in img_url:
    root_dir='img'
    count+=1
    #如果路徑不存在
    if not os.path.exists(root_dir):
        #os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
        os.mkdir(root_dir)
    filname = "now"+str(count)+".jpg"
    #圖URL,存放地址,回掉函數
    request.urlretrieve(img,root_dir+"/"+filname,Sch)
    if count>=16 :
        break


