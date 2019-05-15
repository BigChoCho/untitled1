#豆瓣電影使用滾輪自動加載並且不斷獲取節點

from bs4 import BeautifulSoup
from selenium import webdriver
import time


# # 閱覽訊息用
# content=soup.prettify()
# print(content)


def frist():

    titlist = []
    #解析完才能執行下一步
    driver.implicitly_wait(3)
    # 解析網頁訊息(包跨隱藏項目)
    soup = BeautifulSoup(driver.page_source, 'xml')
    title = soup.find_all("div",{"class":"movie-info"})
    for tit in title:
        #此點下所有子點
        titn = tit.children
        for tits in titn:
            #此點下所有匹配
            if tits.find_all("span",{"class":"movie-name-text"}):
                titlist.append(tits)
                # print(tits.get_text().strip())
    findtit=titlist[len(titlist)-1]
    print(findtit)
    # MoveLoding(findtit)

def MoveLoding(findtit):
    # 向下滚动10000像素
    js = 'document.documentElement.scrollTop=15000'
    driver.execute_script(js)
    time.sleep(10)
    driver.g
    # findtits=findtit.next_elements
    # for i in findtits:
    #     print(i)

    # driver.quit()


if __name__ == '__main__':
    url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
    driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
    driver.get(url)
    frist()