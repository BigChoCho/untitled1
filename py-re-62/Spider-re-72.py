#豆瓣登入
#善用等待時間已切換登入方式

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

url = "https://accounts.douban.com/login?alias=&redir=https%3A%2F%2Fwww.douban.com%2F&source=index_nav&error=1001"

driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
driver.get(url)
#有時候可能因為時間加載問題導致找度到元素
time.sleep(10)
#切換密碼頁
driver.find_element_by_xpath("//li[@class='account-tab-account']").click()
time.sleep(5)
driver.find_element_by_id("username").send_keys("+886972956007")
driver.find_element_by_id("password").send_keys("menpizzerpower")
driver.find_element_by_xpath("//a[@class='btn btn-account btn-active']").click()

driver.save_screenshot("spider-re-72.png")

time.sleep(5)

driver.save_screenshot("spider-re-72-2.png")

with open("spider-re-72.html", 'w', encoding='utf-8') as file:
    #獲取當前網頁訊息並寫入
    file.write(driver.page_source)

driver.quit()
