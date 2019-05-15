
# 運用 requests.post發送請求
import json
import requests
baseurl ="https://fanyi.baidu.com/sug"

wd =input("input your keyword")
data={
    "kw":wd
}


#請求頭
headers = {

    "Content-Length": str(len(data))
}
#requests模塊的data不用轉成byts型的,dit即可,headers需要是str型
rsp =requests.post(baseurl,data=data,headers=headers)

# 讀出來+解碼(獲取到json格式黨)
print(rsp.text)
print(rsp.json())
#
# for item in json_data["data"]:
#     print(item["k"],item["v"])