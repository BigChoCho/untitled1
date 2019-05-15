#UR ERRO

from urllib import request,error,parse

if __name__ == "__main__":
    url = "https://fanyi.baidu.com/sug"

    wd = input("input your keyword")
    data = {
        "kw": wd
    }
    # 轉換url編碼(例如把中文轉成編碼形式)返回默認編碼
    data = parse.urlencode(data).encode()
    # 請求頭
    headers = {

        "Content-Length": len(data)
    }

    try:
        req =request.Request(url=url,data=data,headers=headers)
        rsp = request.urlopen(req)
        html =rsp.read().decode()
        print("獲取成功")
        print(html)

    # 為URLError的子類(會優先處理),http400以上會報錯
    except error.HTTPError as e:
        print("HTTP錯誤問題", e.reason)
        #目前測試為網址有問題,或沒網路
    except error.URLError as  e:
        print("錯誤訊息",e.reason)

        #目前測試為代碼有問題
    except Exception as e:
        print("捕獲",e)