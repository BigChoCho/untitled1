#分析我愛翻譯
#找到XHR(sug)in the Network
#返回格式內容 = json
import json
from urllib import request,parse

baseurl ="https://zhcnt.ilovetranslation.com/web_system/ilovetranslation_com/wwwroot/key/baidu/save/?ajaxtimestamp=1556694191658"

# wd =input("input your keyword")
data={
    "fy_nr": "dog",
    "y_s_y_y": "auto",
    "m_b_y_y": "cht"
}
# 轉換url編碼(例如把中文轉成編碼形式)返回默認編碼
data = parse.urlencode(data).encode("utf-8")
print(data)
#請求頭
headers = {

    "Content-Length": len(data)
}
req =request.Request(url=baseurl,data=data,headers=headers)

#有了headers,data,url就可以發出請求了
rsp =request.urlopen(req)
print(type(rsp))
# 讀出來+解碼(獲取到json格式黨)
json_data =rsp.read().decode("utf-8")


# print(json_data)
#把json字符轉成字典
json_data=json.loads(json_data)
print(json_data)
print(type(json_data))