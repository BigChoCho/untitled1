import requests

#requests用法
url = "https://www.baidu.com/s?"

kw ={
    "pq":"王八蛋"
}
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36/kDVWnXwb-27"
}
#以requests.request請求
rsp = requests.request("get",url)
#以get請求
rsp =requests.get(url,params=kw,headers=headers)


print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)#返回碼
