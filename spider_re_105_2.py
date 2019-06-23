from selenium import webdriver
import time
from lxml import etree
from pprint import pprint
from  selenium.webdriver.common.keys import Keys
chr = webdriver.Chrome()
chr.get('https://www.google.com.tw')

chr.find_element_by_name('q').send_keys('魯蛇')
time.sleep(1)
chr.find_element_by_class_name('gNO89b').click()
chr.find_element_by_class_name('TbwUpd').click()
time.sleep(3)
html=chr.page_source
tit=etree.HTML(html)
tits = tit.xpath('//p/text()')
pprint(tits)
#獲取cookie
# print(chr.get_cookies())
chr.close()