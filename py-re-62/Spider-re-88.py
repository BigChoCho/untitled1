import  requests ,json
from bs4 import BeautifulSoup

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
}

r = requests.get('http://www.seputu.com/',headers=headers)

soup = BeautifulSoup(r.text,'lxml')
content=[]
#以類名取
for tit in soup.find_all(class_='mulu'):
    #默認節點尋找
    h2 = tit.find('h2')
    if str(h2)=="None":
        pass
    else:
        list =[]
        #只取內容
        h2 = h2.string
        for a in tit.find(class_='box').find_all('a'):
            amame=a.string
            href=a.get('href')
            list.append({'aname':amame,'href':href})
            content.append({'tit':h2,'content':list})
with open('spider_88.json','a',encoding='utf-8')as f:
    #indent=整理格式
    json.dump(content,fp=f,ensure_ascii=False,indent=4)