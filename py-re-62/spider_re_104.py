''''
json地址
https://api.bilibili.com/x/tag/ranking/archives?callback=jqueryCallback_bili_460549195187577&tag_id=28784&rid=122&type=0&pn=1&ps=20
視頻地址:
https://www.bilibili.com/video/av55613036/
'''
import json
import requests
import os

class Spider(object):
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"}
    def GetInfo(self,pag):
        list=[]
        url ='https://api.bilibili.com/x/tag/ranking/archives?callback=jqueryCallback_bili_460549195187577&tag_id=28784&rid=122&type=0&pn={}&ps=20'.format(str(pag))
        print(url)
        res=requests.get(url,headers=self.headers)
        jsons=json.loads(res.text).get('data')
        dicts=jsons['archives']
        for dat in dicts:
            title=dat['title']
            href = 'https://www.bilibili.com/video/av{}/'.format(dat['aid'])
            list.append([title,href])
        return list
#下載視頻
    @classmethod
    def Download(cla,list):
        #反回當前路徑
        nowpath = os.getcwd()
        #拼接地址
        paths = os.path.join(nowpath,'bilvideo')
        #判斷是否存在該文件(也可以加上副檔名判斷是否存在文件)
        exis = os.path.exists(paths)
        if exis == False:
            print('不存在資料夾,自動創建....')
            os.mkdir(paths)
        #建立存放路徑
        for title,href in list:
            savevideo=paths+"\\"+title
            print(savevideo)
            print('正在下載{}'.format(title))
            #執行系統操作,you-get進行下載(路徑,視頻地址)
            os.system('you-get -o{} {}'.format(savevideo,href))
            print(title,'下載完成')

if __name__ =="__main__":
    spider=Spider()
    spider.Download(spider.GetInfo(1))