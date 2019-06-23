#地點詳情檢索服務
#http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求
#圓形區域檢索
# http://api.map.baidu.com/place/v2/search?
#百度
import requests
import json
#loc = 行政區域
miyiu= input('密鑰')
def GetJson(loc,page_num):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    #請求訊息
    datas={'query':'城市',
          'region':loc,
          'scope':'2',
          'page_size':20,
          'page_num':page_num,
          'output':'json',
          'ak':miyiu
    }
    url ='http://api.map.baidu.com/place/v2/search?'
    response = requests.get(url,params=datas,headers=headers)
    print(response.url)
    #解碼json返回格式
    getjson = json.loads(response.text)
    return getjson
#河北省,山西省,辽宁省,吉林省,黑龙江省,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,海南省,四川省,贵州省,云南省,陕西省,甘肃省,青海省,台湾省
#從省分獲取城市
city_list= ['河北省','河南省','安徽省','辽宁省','四川省','广东省',]
for cityall in city_list:
    #發送請求返回json格式
    citys=GetJson(cityall,0)
    #獲取當前json格式省的的results
    for seachcity in citys['results']:
        print(seachcity)
        city = seachcity['name']
        num = seachcity['num']
        input = '\t'.join([city,str(num)])+'\n'
        with open('citys.text','a',encoding='utf-8')as f:
            f.write(input)