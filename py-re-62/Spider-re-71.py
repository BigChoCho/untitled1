from selenium import webdriver
import time
from bs4 import  BeautifulSoup


def get_wed(url):
    driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
    driver.get(url)
    print('waitting for .......')
    time.sleep(10)
    print('waitting done .......')

    # 截圖
    driver.save_screenshot('spider-re-71-1.png')
    #欲創建html的檔名
    fn = 'spider-re-71.html'
    with open(fn,"w",encoding="utf-8")as f:
        #driver.page_source=頁面源碼
        f.write(driver.page_source)
    driver.quit()
    #傳入fn(剛創建的html檔)
    content_parse(fn)

def content_parse(fn):
    #讀出資料
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
        # 用bs解析
    soup = BeautifulSoup(html, 'lxml')
    tr1 = soup.select("h4[class='recruit-title']")
    for tr in tr1:
        print(tr.get_text())












if __name__ == '__main__':
    url ="https://careers.tencent.com/search.html?pcid=40002"
    get_wed(url)
