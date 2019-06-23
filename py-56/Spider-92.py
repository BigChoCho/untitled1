from selenium  import webdriver
import time
#開瀏覽器爬蟲可能導致資源消耗過大
# 通過keys模擬鍵盤
from selenium.webdriver.common.keys import Keys

#path用
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')

# 操作一個瀏覽器建立實例(按照環境變量尋找相應瀏覽器)
#如果沒有需要指定位置
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

# 從UI中獲取id=wrapper的內容
text = driver.find_element_by_id('wrapper').text
print(text)
print(driver.title)
#截圖(圖片名)
driver.save_screenshot('index.png')
#找到id"kw"(是百度的輸入框),並且寫入
driver.find_element_by_id('kw').send_keys(u"狗")
#id=su是百度的搜索按鈕,找到並點擊
driver.find_element_by_id('su').click()
#等待獲取頁面
time.sleep(5)
# 得到頁面的快照
driver.save_screenshot('xpng.png')
#獲取當前cookie
print(driver.get_cookies())
#模擬輸入兩個按鍵 ctrl+a(對輸入框進行全選)
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
#剪切 ctrl+x
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.find_element_by_id('kw').send_keys(u"bigtits")
driver.save_screenshot('bigbig.png')
#迴車建
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot('bigbig2.png')
#清空輸入框
driver.find_element_by_id('kw').clear()
driver.save_screenshot('clear.png')

#不用要關閉網頁
driver.quit()
