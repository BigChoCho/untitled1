from urllib import request
import chardet
if __name__=="__main__":
    url ="https://tripmoment.com/Trip/18919"
    rsp= request.urlopen(url)
    #讀取內容為bytes
    #讀取返回結果
    html =rsp.read()
    # 使用chardet進行自動檢測邊碼格式(可能會有誤)
    cs = chardet.detect(html)
    # 必須把bytes轉成字符串(尋找的鑰匙,如果找不到改用默認utf8
    html=html.decode(cs.get("encoding","utf-8"))
    print(html)