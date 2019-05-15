import urllib

if __name__=="__main__":
    url ="https://tripmoment.com/Trip/18919"
    rsp= urllib.request.urlopen(url)

    print("URL: ",rsp.geturl())
    print("info:",rsp.info())
    print("code:",rsp.getcode())
    # 寫出來
    html =rsp.read()

    # 默認編碼
    html =html.decode()
    # print(html)

