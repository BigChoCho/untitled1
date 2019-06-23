from selenium import webdriver
import mongo_demo
#條件發起,觸發
from selenium.webdriver.support import expected_conditions as EC
#設置等待
from selenium.webdriver.support.ui import WebDriverWait
import time
#捕獲超時異常
from  selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def Search():
    browser.get('https://www.jd.com/2017')
    try:
        '''
        EC為條件促發器, until為程序每隔xx秒看一眼，如果条件成立了，
        则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
        By.CSS_SELECTOR 為使用CSS查詢元素
        '''
        #所有元素
        input=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#key')))
        print(input)
        #要點擊的元素
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#search > div > div.form > button')))
        #輸入值
        input[0].send_keys('情趣用品')
        submit.click()
        #銷量紐
        button1= wait.until((EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_filter > div.f-line.top > div.f-sort > a:nth-child(2)'))))
        button1.click()
        #獲取頁數
        page = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#J_bottomPage > span.p-skip > em:nth-child(1) > b')))
        print(page[0].text)
        return  page[0].text
        #在特定时间内未加载页面时,将抛出TimeoutException
    except TimeoutException :
        Search()
def NextPage(pagenume):
    #網頁滾到底
    try:
        browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        time.sleep(3)
        #解析網頁
        html=browser.page_source
        parse_html(html)
        #點擊下一頁
        button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_bottomPage > span.p-num > a.pn-next')))
        button.click()
    except TimeoutException:
        return NextPage(pagenume)
def parse_html(html):
    #解析網頁
    data={}
    soup = BeautifulSoup(html,'lxml')
    goods = soup.select('.gl-item')
    #查看商品數量
    print(len(goods))
    #商品訊息
    for good in goods:
        titles= good.select('.p-name.p-name-type-2 a em')[0].text.strip()
        data['_id']=titles
        pricr = int(float(good.select('.p-price i')[0].text.strip()))
        data['pricr']=pricr
        commit = good.select('.p-commit strong')[0].text.strip()
        commit=commit.replace('条评价','')
        if '万' in commit:
            commit.split('万')
            commit= int(float(commit[0])*10000)
        else:
            commit= int(float(commit.replace('+','')))
        data['commit'] = commit

    #獲取店鋪屬性
        gin = good.select('.goods-icons.J-picon-tips.J-picon-fix')
        if len(gin)>=1:
            mss = gin[0].text.strip()
        else:
             mss='非自營'
        data['mss']= mss
        print(data)
    #存入數據庫
        mogo.to_mongodb(data)

def main():
    search=int(Search())
    for i in range(1,search):
        print('第',i)
        time.sleep(10)
        NextPage(i)
if __name__=='__main__':
    # mongo_demo.MongoMod.to_mongodb()
    browser = webdriver.Chrome()
    '''
    在抛出TimeoutException异常之前将等待X秒或者在X秒内发现了查找的元素。 
    WebDriverWait 默认情况下会每500毫秒调用一次ExpectedCondition直到结果成功返回。
    '''
    wait = WebDriverWait(browser, 10)
    mogo = mongo_demo.MongoMod('127.0.0.1',27017,'sp107','jd')
    main()
