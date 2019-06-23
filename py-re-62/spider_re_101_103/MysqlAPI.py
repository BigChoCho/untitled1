import pymysql

db= pymysql.connect('127.0.0.1','root','111','baidu_map')
cursor =db.cursor()
# TIMESTAMP DEFAULT CURRENT_TIMESTAMP //自動更新
# tables= '''
#         CREATE TABLE park(
#         id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#         uid VARCHAR(200),
#         street_id VARCHAR(200),
#         name VARCHAR(200),
#         address VARCHAR(200),
#         detail_url VARCHAR(200),
#         content_tag VARCHAR(200),
#         create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#         '''
# cursor.execute(tables)
# db.commit()
class Sql():
    #免實例化,免self
    @staticmethod
    def Insert(city,park,lat,lng,address,street_id,uid):
        key= '(city,park,location_lat,location_lng,addres,street_id,uid)'
        # insert = 'INSERT INTO city'+key+ 'VALUES('+'"'+city+'","'+park+'",'+str(lat)+','+str(lng)+',"'+address+'","'+street_id+'","'+uid+'");'
        # print(insert)
        insert= 'INSERT INTO city {} VALUE("{}","{}",{},{},"{}","{}","{}");'.format(key,city,park,lat,lng,address,street_id,uid)

        # print(insert)
        try:
            cursor.execute(insert)
            db.commit()
            print(insert)
        except Exception as f:
            db.rollback()
            print(f)
    @classmethod
    def InsertPark(cls,uid,street_id,name,address,detail_url,content_tag):
        key= '(uid,street_id,name,address,detail_url,content_tag)'
        insert= 'INSERT INTO park {} VALUE("{}","{}","{}","{}","{}","{}");'.format(key,uid,street_id,name,address,detail_url,content_tag)
        try:
            cursor.execute(insert)
            db.commit()
            print(insert)
        except Exception as f:
            db.rollback()
            print(f)
        cursor.close()
        db.close()
    @classmethod
    def Red(cls):
        select = 'SELECT uid FROM city WHERE id<50;'
        try:
            cursor.execute(select)
            db.commit()
            uid=cursor.fetchall()
            print(uid)
            return uid
        except Exception as f:
            db.rollback()
            print(f)
        cursor.close()
        db.close()

