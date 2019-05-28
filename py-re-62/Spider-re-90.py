import pymysql

db = pymysql.connect('0.0.1.0', 'debian-sys-maint', "RqvDUeS3K4jrXUoC",'ceshi')
print(db)
#創見游標對數據進行操作
cursor = db.cursor()
#進行查詢
cursor.execute('select * from BJT')
#接收數據
data =cursor.fetchall()
for i in data:
    print(i)
cursor.close()#關閉游標
db.close()#關閉數據庫