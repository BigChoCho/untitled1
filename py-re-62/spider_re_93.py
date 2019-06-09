
import calendar
import  requests,re
from bs4 import  BeautifulSoup
months=int(input('輸入欲抓取月份'))
moth=calendar.monthrange(2019,months)

headers ={'User-Agent':"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

uels=['https://www.pexels.com/?seed=2019-{}-{}'.format(str(months),str(i)) for i in range (moth[0]-3,moth[1]-26)  ]
sresets=[]
for url in uels:
    # print(url)
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text,'lxml')
    imgs = soup.select('article.photo-item a img')
    for img in imgs:
        srcset= img.get('srcset')
        if srcset != None:
            srcset=srcset.split()[2]
            sresets.append(srcset)
path =r'C:\Users\a3858\PycharmProjects\untitled1\py-re-62\img'
for item in sresets:
    #下載網頁圖片(圖片為二進制的類型,圖片的每個像數格都是以二進制表示顏色)
    data = requests.get(item,headers=headers)

    # print(data.content)
    ##findall(匹配完所有才返回)\d(匹配一個數位字元。等價於[0-9]。)+(直到下一次非數字為止為一群)
# \/(.*?)\?(匹配/開始到?結束)
    photoname = re.findall('\d+\/(.*?)\?',item)[0]
    #判斷是否存在該名
    if photoname:
        fp = open(path+"\\"+photoname,'wb')
        #content代表返回二進制數據
        fp.write(data.content)
        fp.close()
        print('接收到',photoname)
    else:
        print('失敗',item)










