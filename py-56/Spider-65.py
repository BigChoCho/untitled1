'''
使用代理访问百度网站
利用隨機IP訪問或多個代理訪問,避免頻繁訪問(隱藏自己是機器人的身分)
'''
from urllib import  request, error

if __name__ == '__main__':
    url = "http://www.google.com/"
    # 設置代理地址(這個地址可能被多次訪問,導致對方拒絕這個代理)
    proxy ={"http":"221.1.205.74:8060"}
    #創建地址
    proxy_handler = request.ProxyHandler(proxy)
    #實例opener
    opener = request.build_opener(proxy_handler)
    #安裝opener
    request.install_opener(opener)
    try:
        # req =request.Request(url)
        # req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")

        rsp =request.urlopen(url)
        html =rsp.read().decode("utf-8")
        print(html)
    except error.HTTPError as e:
        print("HTTP錯誤問題", e.reason)
        # 目前測試為網址有問題,或沒網路
    except error.URLError as  e:
        print("錯誤訊息", e.reason)

        # 目前測試為代碼有問題
    except Exception as e:
        print("捕獲", e)
