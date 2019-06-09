import requests
from lxml import etree

class Spider(object):
    def __init__(self):
        self.headers = {
        'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    def Main(self,url):
        html = requests.get(url,headers =self.headers)
        ibaotu= etree.HTML(html.text)
        mp4_href =ibaotu.xpath('//div[@class="video-play"]/video/@src')
        titls = ibaotu.xpath('//div[@class="show-image"]/img/@alt')
        self.Write(mp4_href,titls)
    def Write(self,mp4_href,titls):
            for mp4,tit in zip(mp4_href,titls):
                video = requests.get('http:'+mp4,headers=self.headers)
                filname = tit+'.mp4'

                with open(r'C:\Users\a3858\PycharmProjects\untitled1\py-re-62\ibaotu_movie\\'+filname,'wb')as f:
                    #content以進制寫入
                    f.write(video.content)
                    print(filname,'，完成')


if __name__=="__main__":
    spider= Spider()
    for i in range(1,2):
        url ="https://ibaotu.com/shipin/7-0-0-0-0-{}.html".format(str(i))
        spider.Main(url)