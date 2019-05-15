#861登入方式,手動輸入驗證法

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time

url = "http://www.kt861.com.tw/member.php"

driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')
driver.get(url)
#有時候可能因為時間加載問題導致找度到元素
time.sleep(5)
code = input("輸入驗證碼")
#切換密碼頁
time.sleep(5)
driver.find_element_by_name("mm_account").send_keys("0921340917")
driver.find_element_by_name("mm_password").send_keys("menpizzerpower")
driver.find_element_by_xpath("//input[@class='ipt2 iptbox']").send_keys(code)
time.sleep(3)
driver.find_element_by_xpath("//input[@class='shop_btn']").click()
time.sleep(10)




driver.quit()
