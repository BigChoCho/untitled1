import  pymongo
#本地訪問
client = pymongo.MongoClient()
#創建庫
db = client.spider
post = {
    'name':'王曉明',
    'sex':'m',
    'age':'18',
    'class':['學生','酒店','外送茶','牛郎','直播'],
    'income':'12223'
}
#實例
#db.posts的posts是創建的表名稱
posts = db.posts
#對表插入集合數據
post_id = posts.insert_one(post).inserted_id