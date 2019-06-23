#地點詳情檢索服務
#http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求
#圓形區域檢索
# http://api.map.baidu.com/place/v2/search?
#百度
import requests
#loc = 行政區域
miyiu= input('密鑰')

def GetJson(loc,page_num):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    datas={'query':'公園',
          'region':loc,
          'scope':'2',
          'page_size':20,
          'page_num':page_num,
          'output':'json',
          'ak':miyiu
    }
    url ='http://api.map.baidu.com/place/v2/search?'
    response = requests.get(url,params=datas,headers=headers)
    getjson = response.json()
    print(response.url)
    return getjson

newjson = GetJson('10428',0)

print(newjson)