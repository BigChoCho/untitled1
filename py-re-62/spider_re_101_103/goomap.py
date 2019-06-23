import googlemaps
import pprint
import time
key= input('key:')
gmaps = googlemaps.Client(key=key)

#location:搜尋位置的經緯度,radius:搜尋的半徑以米為單位open_now:是否獲取地點詳情,查找的例如convenience_store(便利商店)
#type英文對應關係的網頁:https://developers.google.com/places/web-service/supported_types
places_result = gmaps.places_nearby(location='25.114842, 121.516219',radius=1000,open_now=False,type='convenience_store')
#pprint.pprint:將返回的對象格式化
pprint.pprint(places_result)
#當你想要獲取下一組訊息時必須給google一些加載訊息的時間,不然有時候會加載失敗
time.sleep(3)
#當你發出請求後並且獲取訊息,會得到一個next_page_token的令牌,使用這一組令牌來訪問下一組訊息
#請求下一組數據最多返回20條訊息
print("____"*10+"第二頁")
places_result = gmaps.places_nearby(page_token=places_result['next_page_token'])
pprint.pprint(places_result)
print("____"*10+"請求詳情")
time.sleep(3)
# 這邊先建立等等要獲取的詳情key
info = ['name', 'photo']
#藉由獲取results 的key,比喻:如同撥開一層層的洋蔥,得以獲得裡面的k,v值,如果不這樣做它只能獲取最外層的k,v
for place in places_result['results']:
    #獲取便利商店的ID,可用此ID進一步獲取詳情訊息
    place_id=place['place_id']

    #不填寫fields ,表示返回所有詳情
    datalist = gmaps.place(place_id=place_id,fields=info)
    pprint.pprint(datalist)