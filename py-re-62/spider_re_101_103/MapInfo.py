import requests
import json
from MysqlAPI import Sql
#城市公園訊息
#詳情索引
#http://api.map.baidu.com/place/v2/detail?uid=379a3f0e864e7f5039221cb9&output=json&scope=2&ak=您的密钥 //GET请求
def GetCity():
    city_list=[]
    #讀取內容獲取程式碼
    with open('citys.text','r',encoding='utf-8')as f:
        for search in f:
            fileds= search.split('\t')
            city = fileds[0]
            num = fileds[1]
            city_list.append(city)
    return city_list
def GetJson(loc,page_num):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    #請求訊息
    datas={'query':'銀行',
          'region':loc,
          'scope':'2',
          'page_size':20,
          'page_num':page_num,
          'output':'json',
          'ak':miyiu
    }
    url ='http://api.map.baidu.com/place/v2/search?'
    response = requests.get(url,params=datas,headers=headers)
    getjson = json.loads(response.text)
    return getjson    #解碼json返回格式
if __name__ =="__main__":
    miyiu = input('密鑰')
    citys=GetCity()
    for city in citys:
       parks =GetJson(city,0)
       #判斷是否存在公園
       if 'results' in parks:
           for parkinfo in parks['results']:
               try:
                   #公園名稱
                   park=parkinfo['name']
               except:
                    park="None"
               try:
                   #座標
                   lat = parkinfo['location']['lat']
               except:
                    lat="None"
               try:
                   lng = parkinfo['location']['lng']
               except:
                    lng = "None"
               try:
                   address=parkinfo['address']
               except:
                   address="None"
               try:
                   street_id = parkinfo['street_id']
               except:
                   street_id = "None"
               try:
                    uid= parkinfo['uid']
               except:
                   uid="None"


               Sql.Insert(city,park,lat,lng,address,street_id,uid)

