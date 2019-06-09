# https://music.163.com/discover/artist/cat?id=1001&initial=0
# id=1001 區域 女歌手,歐美歌手....
# initial=66 類A.B.C.D....
import requests
from bs4 import BeautifulSoup
import csv
def get_artists(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
        ,"Host":"music.163.com",
        "Referer":"https://music.163.com/"
    }
    reponse = requests.get(url,headers=headers)
    soup = BeautifulSoup(reponse.text,'lxml')
    #attrs 参数定义一个字典参数来搜索包含特殊属性的tag:
    #a節點下 class:class的值
    for item in soup.find_all('a',attrs={'class':'nm nm-icn f-thide s-fc0'}):
        name = item.string.strip()
        #replace省略值strip()去除括號類指令字符串
        id =item['href'].replace('/artist?id=','').strip()
        print(name,id)
        try:
            #將row參數寫入writer的文件對象，根據當前方言進行格式化(行)
            write.writerow((name,id))
        except Exception as f:
            print('錯誤',f)

if __name__=="__main__":
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 7001, 7002, 7003, 4001, 4002, 4003]
    init_list = [-1, 0]
    csvfile = open('music163.csv','a',encoding='utf-8')
    write = csv.writer(csvfile)

    for i in range(65, 91): init_list.append(i)
    url = "https://music.163.com/discover/artist/cat?id={}&initial={}".format(str(id_list[0]),str(init_list[2]))
    get_artists(url)