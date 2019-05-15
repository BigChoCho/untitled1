from bs4 import BeautifulSoup
from selenium import webdriver
import time

class Douyu():
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
        self.url = 'https://www.douyu.com/'

    def douyu(self):
        self.driver.get(self.url)
        while True:
            soup = BeautifulSoup(self.driver.page_source, 'xml')
            titles = soup.find_all('h3', {'class': 'DyCover-intro'})
            nums = soup.find_all('span', {'class': 'DyCover-hot'})
            for title, num in zip(titles, nums):
                print("(房間):{0} (人数):{1}".format(title.get_text().strip(), num.get_text().strip()))
                #判斷當前字符串是否有在獲取當前節點的內容中
                if "全程激情" in title.get_text().strip() :
                    #previous_elements=所有前面的節點
                    for tit in title.previous_elements:
                        #find_previous = 利用previous_elements迭代後進行tag匹配
                        tits=tit.find_previous("a")
                        time.sleep(2)
                        #獲取匹配後的當前對象中的一個屬性的內容
                        print(tits.get('href'))
                        #抓到最後一個網址的導向地址就可以返回,然後拼湊整段網址進行訪問
                        self.driver.quit()
            time.sleep(20)

    def destr(self):
        self.driver.quit()

if __name__ == '__main__':
    douyu = Douyu()
    douyu.setUp()
    douyu.douyu()
    douyu.destr()






