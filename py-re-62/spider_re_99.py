# https://www.ximalaya.com/revision/play/album?albumId=22629331&pageNum=1&sort=1&pageSize=30
# https://www.ximalaya.com/revision/play/album?albumId=291718&pageNum=1&sort=1&pageSize=30

#https://www.ximalaya.com/yinyue/
#更改後面網址以對應欲爬取內容
import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    def GetReponce(self,url):
        reponce = requests.get(url, headers=self.headers)
        return reponce
    def Main(self,reponce,id):
        try:
            list =[]
            htmls = etree.HTML(reponce.text)

            datas = htmls.xpath("//a[@class='album-title line-1 lg bold _kC']")
            for data in datas:
                tits = data.xpath('./@title')
                href = data.xpath('./@href')
                id+=1
                list.append("id("+str(id)+'):'+tits[0].strip()+href[0])
            print(list)
            idnum=int(input('輸入欲抓取該音樂整套輯的id:'))
            idnum=list[idnum-1].split('/')
            return idnum[-2]
        except Exception as f:
            print('拼音內容可能有誤,或無法對應該拚音,請重新運行'+f)
            return ""
    def GetJson(self,reponce):
        import re
        json=reponce.text
        trackName = re.findall(r'"trackName":(.*?),',json)
        src = re.findall(r'"src":(.*?),',json)
        # print(src)
        print(trackName)
        return src ,trackName
    def DownLoad(self,src ,trackName):
        import os
        #在當前路徑中生成資料夾(放置音樂用)
        paths = os.getcwd()
        paths = os.path.join(paths, '自定義')
        print(paths)
        #判斷文件夾是否存在
        being = os.path.exists(paths)
        if being == False:
            print('建立資料夾')
            os.mkdir(paths)
        for m4a,name in zip(src,trackName):
            music = requests.get(m4a.strip('"'), headers=self.headers)
            name =name.strip('"')
            with open(paths+"\\"+name+'.m4a','wb')as f:
                f.write(music.content)
                print(name,'下載完畢')
        print('DONE')
        stop=input('等待')



def Pini(music):
    from pypinyin import lazy_pinyin

    music = lazy_pinyin(music)
    if len(music):
        music = ''.join(music) + "/"
    else:
        music = ""
    return music
if __name__ == '__main__':
    idnum = 0
    music=input('請輸入音樂爬取的音樂總類,不輸入表示音樂全部種類:')
    pini=Pini(music)
    url = "https://www.ximalaya.com/yinyue/{}".format(pini)
    spider=Spider()

    reponce=spider.GetReponce(url)
    idnumber_url="https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=1&pageSize=30".format(spider.Main(reponce,idnum))
    src,trackName=spider.GetJson(spider.GetReponce(idnumber_url))
    spider.DownLoad(src,trackName)