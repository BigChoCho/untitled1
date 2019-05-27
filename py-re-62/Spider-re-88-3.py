import  requests
import csv
from lxml import etree
import re

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
}

r = requests.get('http://www.seputu.com/',headers=headers)

html = etree.HTML(r.text)
rows=[]
titall = html.xpath('//*[@class="mulu"]')
for tit in titall:
    h2=tit.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    if len(h2):
        h2tit = h2
        a_s =tit.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            tits = a.xpath('./@title')[0]
            #匹配所有
            pattern = re.compile(r'\s*\[(.*)]\s+(.*)')
            match = pattern.search(tits)
            if match !=None:
                #抓出時間
                data = match.group(1)
                real_title = match.group(2)
                content = (h2tit,real_title,href,data)
                rows.append(content)
#寫入csv中
#csv使用於excle時需轉換格式,詳見PythonExcle
headtit = ['大標題','項目','網址','日期']
with open('spider_88_3.csv','w',encoding='utf-8',newline="")as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headtit)
    # 寫入多行
    f_csv.writerows(rows)