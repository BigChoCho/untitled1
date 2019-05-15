#百度資料
#找到XHR(sug)in the Network
#返回格式內容 = json
import json
from urllib import request,parse

baseurl ="https://fanyi.baidu.com/sug"

wd =input("input your keyword")
data={
    "kw":wd
}
# 轉換url編碼(例如把中文轉成編碼形式)返回默認編碼
data = parse.urlencode(data).encode()
print(len(data))
#請求頭
headers = {

    "Content-Length": len(data)
}
#有了headers,data,url就可以發出請求了
rsp =request.urlopen(baseurl,data=data,)

# 讀出來+解碼(獲取到json格式黨)
json_data =rsp.read().decode()
print(json_data)
print(type(json_data))
#把json字符轉成字典
json_data=json.loads(json_data)
print(type(json_data))
print(json_data)
for item in json_data["data"]:
    print(item["k"],item["v"])