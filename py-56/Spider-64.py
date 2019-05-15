'''
访问一个网址
更改自己的UserAgent进行伪装
'''
from urllib import request, error

if __name__ == '__main__':

    url = "http://www.baidu.com"

    try:
        # 第一種方法
        # headers = {}
        # #模擬成ipad.os系統
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'
        # #模擬
        # req =request.Request(url,headers=headers)

        #第二種方法
        req =request.Request(url)
        #模擬成windows系統,Chrome的瀏覽器(以添加的方式執行)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")

        #開始進行訪問與讀取
        rsp = request.urlopen(req)
        html =rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print("HTTP錯誤問題", e.reason)
        # 目前測試為網址有問題,或沒網路
    except error.URLError as  e:
        print("錯誤訊息", e.reason)

        # 目前測試為代碼有問題
    except Exception as e:
        print("捕獲", e)
