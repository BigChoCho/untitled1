'''
构建代理集群/队列
每次访问服务器，自動循環,跳開不能使用的proxy
抽取可以使用 random.choice

分析步骤：
1. 构建代理群
2.源端關閉不見得是proxy的問題,有可能是沒有模仿模擬瀏覽器的問題
'''

from urllib import request, error
import random
import time
#構建多個代理
proxy_list=[
    {"http":"47.107.160.99:8118"},
    {"http":"114.221.80.3:8118"},
    {"http":"124.128.76.142:8060"},
    {"http":"121.17.210.114:8060"},
    {"http":"163.125.66.95:9797"},
    {"http":"60.217.153.74:8060"}
]
# 2. 创建ProxyHandler
proxy_handler_list = []
for prxo in proxy_list:
    #传入一个代理，这个代理是一个字典：
    proxy_handler = request.ProxyHandler(prxo)
    #將傳入的代理加入空數組
    proxy_handler_list.append(proxy_handler)
print(proxy_handler_list)

# 3. 创建Opener
opener_list = []
for poxyhander in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
print(opener_list)

url = "http://www.baidu.com"
count = 0
opener2 =[]
while count<6:
    # if len(opener2)>=6:break
# 现在如果访问url，则使用代理服务器
    try:
        # 4. 安装Opener
        #choice= 重置抽樣，有機會抽到相同的元素
        opener = opener_list[count]
        print("當前使用的proxy",opener)
        # if opener in opener2:
        #     continue
        #安裝代理
        request.install_opener(opener)
        opener2.append(opener)
        #開起網頁
        time.sleep(5)
        #如果此時產生異常,則會促發except重新開始一次
        rsp = request.urlopen(url)
        #寫出網頁訊息
        html = rsp.read().decode()
        print(html)
        #沒異常就會跑到這裡
        break
    except error.URLError as e:
        print("URL",e)
        count+=1
    except Exception as e:
        print("EXCP",e)
        count+=1
