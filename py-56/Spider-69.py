from urllib import request, parse
from http import cookiejar

#  创建cookiejar的实例
filename = "cookie.txt"
#保存cookie
cookie = cookiejar.MozillaCookieJar()
# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    #發送登入訊息的網址
    # (在源碼中找到帳密框的(form)找到action發送登入訊息的網址
    url="http://www.renren.com/PLogin.do"
    #輸入的用戶訊息  action(找到input,name類型的鍵)
    data ={
        "email":"13119144223",
        "password":"123456"

    }
    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求(登入並從對請求管理器獲取coikie)
    #打開後保存cookie文件
    rsp = opener.open(req)
    #保存cookie到文件(即使cookie要把瀏覽器丟棄,也要保存下來 , 過期也要保存)
    cookie.save(ignore_discard=True,ignore_expires=True)


if __name__ =="__main__":
    login()
    # print(cookie)
    # for item in cookie:
    #     print(type(item))
    #     print(item)
    #     for i in item:
    #         print(i)
