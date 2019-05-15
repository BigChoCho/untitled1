from selenium  import webdriver
import time
import json
#GOOGLE
#開瀏覽器爬蟲可能導致資源消耗過大
# 通過keys模擬鍵盤
from selenium.webdriver.common.keys import Keys

#path用
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument('--headless')

# 操作一個瀏覽器建立實例(按照環境變量尋找相應瀏覽器)
#如果沒有需要指定位置
driver = webdriver.Chrome(r'C:\Users\a3858\PycharmProjects\untitled1\chromedriver.exe')

driver.get("https://tw.match.com/logout")

#截圖(圖片名)
driver.save_screenshot('index.png')
#找到id"kw"(是百度的輸入框),並且寫入
driver.find_element_by_name("email").send_keys(u"menpizzer76@gmail.com")
driver.find_element_by_name("password").send_keys(u"menpizzerpower")
time.sleep(3)
#類明如果是複合的,必須尋找唯一,非唯一也可以取其中一個用下標表示
driver.find_element_by_class_name("css-1in3bb8").click()
#等待獲取頁面
time.sleep(5)
# 得到頁面的快照
driver.save_screenshot('xpng.png')
# #獲取當前cookie
cookies=driver.get_cookies()
#需轉換成json格式才可以用list的方式依序寫入
jsonCookies = json.dumps(cookies)

#以json格式寫入
with open("cok-93.json", "w",encoding="utf-8") as f:
    f.write(jsonCookies)

time.sleep(5)
#不用要關閉網頁
driver.quit()
#對JSON格式進行整理
with open('cok-93.json','r',encoding='utf-8') as f:
    listCookies=json.loads(f.read())
cookie = [item["name"] + "=" + item["value"] for item in listCookies]
cookiestr = '; '.join(item for item in cookie)


from urllib import request



url = "https://tw.match.com/search/mutual"
req = request.Request(url)
req.add_header("User-Agent",
               "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
#傳入cookie值
headers ={"Cookie":cookiestr}
req = request.Request(url=url,headers=headers)
rsp = request.urlopen(req)
html = rsp.read().decode("utf-8")
with open("rsp-93.html", "w",encoding="utf-8") as f:
    f.write(html)