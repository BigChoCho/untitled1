import pymysql

db = pymysql.connect('127.0.0.1', 'popo', "111",'mysql_3')
print(db)
#創見游標對數據進行操作
cursor = db.cursor()
#進行mysql的指令語法操作
cursor.execute('SHOW TABLES')
#接收所有數據
data =cursor.fetchall()
for i in data:
    print(i)
cursor.close()#關閉游標
db.close()#關閉數據庫