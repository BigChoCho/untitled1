# https://www.kugou.com/yy/rank/home/23-8888.html?from=rank

#//div[@class='pc_temp_songlist']/ul/li/     span.pc_temp_num  and a

import requests
from bs4 import BeautifulSoup
import time
import pymongo
headers = {
    'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
client = pymongo.MongoClient()
db = client.spider_96.kugou

def Kugou(url,count):
    reponse=requests.get(url,headers=headers)
    soup = BeautifulSoup(reponse.text,'lxml')
    titles = soup.select('.pc_temp_songlist > ul > li > a')
#編號
    number = soup.select('span.pc_temp_num')
#時間
    times = soup.select('span.pc_temp_time')
    for title,num,time in zip(titles,number,times):
        data={
        'num' : num.get_text().strip()
        ,'song':title.get_text().split('-')[1].strip()
        ,'singer':title.get_text().split('-')[0].strip()
        ,'time':time.get_text().strip()
        }
        print(data)
        Mongo(data)
    count+=1
    # print('--'*20+"第{}頁".format(str(count)))
def Mongo(data):

    #插入數據
    id = db.insert(data)
    print(id)
if __name__=='__main__':
#至多24
    for i in range(1,24):
        url ='https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(i)
        Kugou(url,i-1)
        time.sleep(2)

