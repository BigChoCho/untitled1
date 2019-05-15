#破解有道辭典
from urllib import request,parse
def youdao(key):

    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data ={

        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt": "15567998596256",
        "sign":"1b0ba5f65a22bbd58b971640e4629876",
        "ts": "1556799859625",
        "bv": "94d71a52069585850d26a662e1bcef22",
        "doctype":"json",
        "version":"2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTlME"
    }
    #轉碼(data需要是bytes格式)
    data = parse.urlencode(data).encode()

    headers ={


        "Accept":"application/json,text/javascript,*/*;q=0.01",
        # "Accept-Encoding":"gzip,deflate",
        "Accept-Language":"en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Connection":"keep-alive",
        "Content-Length":"234",
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie":"DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|;OUTFOX_SEARCH_USER_ID=1630859404@223.139.136.49;JSESSIONID=abcLiAA6kRTNBbBCYF4Pw; OUTFOX_SEARCH_USER_ID_NCOO=389412825.69642687; ___rl__test__cookies=1556799859623",
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36/CrgfV79q-15",
        "X-Requested-With":"XMLHttpRequest"

    }
    req =request.Request(url=url,data=data,headers=headers)

    rsp =request.urlopen(req)
    html =rsp.read().decode()
    print(html)
if __name__=="__main__":
    youdao("a")