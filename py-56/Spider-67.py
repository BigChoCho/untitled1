from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/"
    req = request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
    #傳入cookie值
    headers ={"Cookie":"PHPSESSID=gvkm60qnmai4ba30ev6gq28sh0"}
    req = request.Request(url=url,headers=headers)

    rsp = request.urlopen(url)

    html = rsp.read().decode("utf-8")

    with open("rsp-3.html", "w",encoding="utf-8") as f:
        f.write(html)