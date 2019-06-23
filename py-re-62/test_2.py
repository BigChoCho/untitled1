import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
url = 'https://sz.lianjia.com/zufang/luohuqu/'
reponse = requests.get(url, headers=headers)
print('網址',reponse.url)
print(reponse.text)