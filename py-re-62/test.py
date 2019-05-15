import re


url ='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557895020042&countryId=1&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=us'
curpage = re.findall('(\d+)', url)
curpage=curpage[2]
page = int(curpage) + 1
url = url.replace("Index=1","Index="+str(page))
print(url)