from selenium import webdriver
#條件發起,觸發
from selenium.webdriver.support import expected_conditions as EC
#設置等待
from selenium.webdriver.support.ui import WebDriverWait
import time
#捕獲超時異常
from  selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

brower =webdriver.Chrome()
#讓窗口最大化
brower.maximize_window()
wait = WebDriverWait(brower,10)
def index_page(page):
    print('第',page)
