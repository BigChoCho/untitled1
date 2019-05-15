import urllib

if __name__=="__main__":
    #  /s?  (參數)
    url ="https://www.baidu.com/s?"
    wd =input("input your keyword")
    # 創建字典
    qs={
        "wd":wd
    }
    # 轉換url編碼(例如把中文轉成編碼形式)
    qs = urllib.parse.urlencode(qs)
    # 拼湊
    fullul= url+qs
    # 打印網址最後樣式
    print(fullul)
    # 打開並搜尋資訊
    rsp= urllib.request.urlopen(fullul)


    # 寫出來
    html =rsp.read()

    # 默認編碼
    html =html.decode()
    print(html)

