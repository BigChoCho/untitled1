

# sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")

def getSalt():
# salt公式:
#把它翻譯成python代碼
    import time ,random
#對方有13個字,我們只有9個所以*1000
    #版本不一,14個的
    salt=str(int(time.time()*1000))+str(random.randint(0,10))
    print("salt=",salt)
#13個的
    # salto=int(time.time()*1000)+random.randint(0,10)
    # print(salto)
    return salt
def getMd5(v):
    #hashlib是加密算法(這邊使用MD5的方式)
    #摘要算法又称为哈希算法，散列算法。它通过一个函数，
    # 把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）用于加密相关的操作。
    import hashlib
    md5 = hashlib.md5()
    #計算md5(傳入的值,給定的編碼)
    md5.update(v.encode("utf-8"))
    #計算摘要
    sign = md5.hexdigest()
    print(sign)
    return  sign
def getSing(key,salt):
    sign = "fanyideskweb" + key + str(salt) + "@6f#X3=cCuncYssPsuRUE"
    sign= getMd5(sign)
    return sign
from urllib import request,parse
def youdao(key):
    salt =getSalt()
    url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data ={

        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":str(salt),
        "sign":getSing(key,salt),
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
        #是否壓縮,不要所以取消
        # "Accept-Encoding":"gzip,deflate",
        "Accept-Language":"en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7",
        "Connection":"keep-alive",
        #data轉碼後的總數
        "Content-Length":len(data),
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
    youdao("fucking")
