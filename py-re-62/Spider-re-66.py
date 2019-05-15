'''
爬取伯乐在线的美女联系方式
需要：
1. 登录
2. 在登录和相应声望值的前提下，提取对方的邮箱
'''

from urllib import request, error, parse
from http import cookiejar
import json

def login():
    """
    输入用户名称和密码
    获取相应的登录cookie
    cookie 写文件
    :return:
    """

    # 1. 需要找到登录入口
    url = "http://www.jobbole.com/wp-admin/admin-ajax.php"

    # 2. 准备登录数据
    data = {
        "action": "user_login",
        "user_login": "augsnano",
        "user_pass": "123456789",
        "remember_me": "1",
        # 登陆后重定向地址
        "redirect_url": "http://date.jobbole.com/4965/"

    }

    data = parse.urlencode(data).encode()


    # 3. 准备存放cookie文件
    # r表示不转义
    f = r'jobbole_cookie.txt'

    # 4. 准备请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
        "Connection": "keep-alive"
    }

    # 5.聲明一个MozillaCookieJar對象實例来保存cookie，之後寫入文件
    cookie_handler = cookiejar.MozillaCookieJar(f)
    print("cookie_handler:",cookie_handler)
    # 6. 准备http请求handler
    http_handler = request.HTTPCookieProcessor(cookie_handler)
    print("HTTP:",http_handler)


    # 7. 构建opener
    opener = request.build_opener(http_handler)

    # 8. 构建请求对象
    req = request.Request(url, data=data, headers=headers)

    # 9. 发送请求
    try:
        rsp = opener.open(req)
        #存cookie
        cookie_handler.save(f, ignore_discard=True, ignore_expires=True)

        html = rsp.read().decode("utf-8")
        print(html)
    except error.URLError as e:
        print(e)


def getInfo():
    # 1. 确定url
    url = "http://date.jobbole.com/wp-admin/admin-ajax.php"

    # 2. 读取已经保存的cookie
    f = r'jobbole_cookie.txt'
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(f, ignore_expires=True, ignore_discard=True)

    # 3. 构建http_handler
    http_handler = request.HTTPCookieProcessor(cookie)

    # 4. 构建opener
    opener = request.build_opener(http_handler)

    # 以下是准备请求对象的过程

    # 5. 构建data
    data = {
        "action": "get_date_contact",
        "postId": "4965"
    }

    data = parse.urlencode(data).encode()

    # 6. 构建请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
        "Connection": "keep-alive"
    }

    # 7. 构建请求实体
    req = request.Request(url, data=data, headers=headers)

    # 8. 用opener打开
    try:
        rsp = opener.open(req)
        html = rsp.read().decode()


        print(html)


        with open("COB.html", 'w') as f:
            f.write(html)

    except Exception as e:
        print("錯誤",e)






if __name__ == '__main__':
    login()