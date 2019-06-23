import pymysql
from  spider_re_116 import settings

MYSQL_HOST=settings.MYSQL_HOST
MYSQL_USER=settings.MYSQL_USER
MYSQL_PASSWORD=settings.MYSQL_PASSWORD
MYSQL_PORT=settings.MYSQL_PORT
MYSQL_DB=settings.MYSQL_DB

db=pymysql.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOST,port = MYSQL_PORT,database = MYSQL_DB)
cursor = db.cursor()
class Sql():

    @classmethod
    def insert(cls,country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime):
        print('Sql insert啟動中')
        sql = 'INSERT INTO xici(country,ipaddress,port,serveraddr,isanonymous,type,alivetime,verifictiontime) VALUES(' \
              '%(country)s,%(ipaddress)s,%(port)s,%(serveraddr)s,%(isanonymous)s,%(type)s,%(alivetime)s,%(verifictiontime)s)'
        value  ={

        "country":country,
        "ipaddress":ipaddress,
        "port":port,
        "serveraddr":serveraddr,
        "isanonymous":isanonymous,
        "type":type,
        "alivetime":alivetime,
        "verifictiontime":verifictiontime
        }
        try:
            cursor.execute(sql,value)
            db.commit()
        except Exception as f:
            print('失敗',f)
            db.rollback()
        print('Sql insert啟動完畢')
        #去重
    @classmethod
    def selct_name(cls,ipaddress):
        print('selct_name啟動')
        #查詢庫中是否以存在該ip,如果存在返回1
        sql = 'select exists(select 1 from xici where ipaddress=%(ipaddress)s)'
        value ={
            'ipaddress':ipaddress
        }
        cursor.execute(sql,value)
        return  cursor.fetchall()[0]
