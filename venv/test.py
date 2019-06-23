import requests
import json
#loc = 行政區域
miyiu= input('密鑰')
def GetJson():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    #請求訊息
    datas={'location':'22.655528, 120.329981',
           'radius':1000,
           'open_now':False,
           'type':'convenience_store',
    }
    url ='https://www.googleapis.com/geolocation/v1/geolocate?key={}'.format(miyiu)
    response = requests.get(url,params=datas,headers=headers)
    print(response.text)
    # #解碼json返回格式
    # getjson = json.loads(response.text)
    # return getjson
if __name__ == "__main__":
    GetJson()