import requests
from lxml import etree
#相對路徑,當前目錄下
import mongomod
mongo_post = mongomod.MongoAPI('127.0.0.1', 27017, 'spider_97', 'hupu')


def spider(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

    res = requests.get(url,headers=headers)
    html =res.text
    html = etree.HTML(html)
    return html
def parse(html):
    htmls=html.xpath('//div[@class="titlelink box"]')
    for datas in htmls:
        titls = datas.xpath('./a/text()')
        hrefs =datas.xpath('./a/@href')
        #有些標題放在節點b，判斷如果不存在內容執行
        if len(titls) ==0:
            titls = datas.xpath('./a/b/text()')
        # print('tit',len(titls))
        #following-sibling 同級別往下搜
        authors = datas.xpath("./following-sibling::div/a[@class='aulink']/text()")
        tims = datas.xpath("./following-sibling::div/a[2]/text()")
        #點閱
        click_rate =datas.xpath("./following-sibling::span/text()")[0].split('/')
        repaly_rate=click_rate[0].strip()
        click_rate = click_rate[1].strip()
        #最後回覆時間
        overtimes = datas.xpath("./following-sibling::div[@class='endreply box']/a/text()")
        overname =  datas.xpath("./following-sibling::div[@class='endreply box']/span/text()")


        InputData(titls[0],'https://bbs.hupu.com'+hrefs[0],authors[0],tims[0],repaly_rate,click_rate,overtimes[0],overname[0])
def InputData(titls,hrefs,authors,tims,repaly_rate,click_rate,overtimes,overname):
    #地址,端口,數據庫,數據表集合
    print(titls,hrefs,authors,tims,repaly_rate,click_rate,overtimes,overname)
    mongo_post.add({
        'titls':titls
        ,'hrefs':hrefs
        ,'authors':authors
        ,'tims':tims
        ,'repaly_rate':repaly_rate
        ,'click_rate':click_rate
        ,'overtimes':overtimes
        ,'overname':overname
    })

def main():

    url="https://bbs.hupu.com/bxj"
    htmls=spider(url)
    parse(htmls)

if __name__ =="__main__":

    main()