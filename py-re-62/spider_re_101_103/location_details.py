#獲取詳情
#http://api.map.baidu.com/place/v2/detail?uid=379a3f0e864e7f5039221cb9&output=json&scope=2&ak=您的密钥 //GET请求
import requests
import json
from MysqlAPI import Sql

def GetJson(uid):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    #請求訊息
    datas={'uid':uid,
          'scope':'2',
          'output':'json',
          'ak':miyiu
    }
    url ='http://api.map.baidu.com/place/v2/detail'
    response = requests.get(url,params=datas,headers=headers)
    getjson = json.loads(response.text)
    return getjson    #解碼json返回格式
if __name__=="__main__":
    miyiu = input('密鑰')
    uids=Sql.Red()
    for uid in uids:
       jsons=GetJson(uid[0])
       if 'result' in jsons:
        infos=jsons['result']
        try:
            uid= infos['uid']
        except:
            uid=None
        try:
            street_id= infos['street_id']
        except:
            street_id=None
        try:
            name= infos['name']
        except:
            name=None
        try:
            address = infos['address']
        except:
            address = None
        try:
            detail_url = infos['detail_info']['detail_url']
        except:
            detail_url = None
        try:
            content_tag = infos['detail_info']['content_tag']
        except:
            content_tag = None
        Sql.InsertPark(uid,street_id,name,address,detail_url,content_tag)