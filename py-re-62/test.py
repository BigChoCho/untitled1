from bs4 import BeautifulSoup
import requests
import json
import pymongo

url = 'http://www.guokr.com/scientific/'


def dealData(url):
    client = pymongo.MongoClient('localhost', 27017)
    guoke = client['guoke']
    guokeData = guoke['guokeData']
    web_data = requests.get(url)
    datas = json.loads(web_data.text)
    print
    datas.keys()
    for data in datas['result']:
        guokeData.insert_one(data)


def start():
    urls = [
        'http://www.guokr.com/apis/minisite/article.json?retrieve_type=by_subject&limit=20&offset={}&_=1508843461033'.format(
            str(i)) for i in range(20, 100, 20)]
    for url in urls:
        dealData(url)


start()
