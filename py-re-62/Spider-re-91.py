
def State():
    import pymysql
    tableoff = False
    tablename =input('輸入欲創建表名or欲插入,查詢,更改的表名')
    # spider=欲使用的數據庫
    us = pymysql.connect('127.0.0.1', 'root', '111', 'spider')
    print(us)
    cursor = us.cursor()
    return cursor ,tablename,tableoff,us

def CreateTable(cursor,tablename,tableoff):
    # 當前庫下所有表
    print(tablename)
    cursor.execute('SHOW TABLES;')
    tables = cursor.fetchall()
    #判斷是否存在
    for table in tables:
        print(table[0])
        if table[0] == tablename:
            print('列表',table[0],'已存在')
            tableoff = True
        #如果不存在,創建
    if not tableoff:
        #PRIMARY KEY AUTO_INCREMENT =主健自增長
        cursor.execute('CREATE TABLE '+tablename+'(id INT PRIMARY KEY AUTO_INCREMENT, firstname VARCHAR(32),lastname VARCHAR(32),age INT,'
                                                 'sex ENUM("M","F"),assets DOUBLE);')
        print('創建成功')

#對表插入值
def InsertValues(cursor,tablename,us):
    while True:
        ent=input('添加值請輸入Y,不添加請輸入任意值:')
        if ent=='Y' or ent =='y':
            firstname='"'+input('輸入姓')+'"'
            lastname ='"'+input('輸入名')+'"'
            age = input('輸入年齡')
            sex = input('輸入M代表男,輸入F代表女,隨意填寫代表男')
            if sex == 'm' or sex =='M':
                sex='M'
                print('男女判定正確')
            elif sex =='f' or sex=='F':
                sex='F'
            else :
                sex='M'
            sex ='"'+sex+'"'
            assets = input('輸入資產')
            print('INSERT INTO '+tablename+"(firstname,lastname,age,sex,assets) VALUSE"+"("+firstname+","+lastname+","+age+","+sex+","+assets+");")
            cursor.execute('INSERT INTO '+tablename+"(firstname,lastname,age,sex,assets) VALUES"+"("+firstname+","+lastname+","+age+","+sex+","+assets+");")
            print('持續添加')
        else :
            print('exit')
            cursor.execute('SELECT * FROM '+tablename+";")
            nowselecttable=cursor.fetchall();
            #顯示表內容
            print('表:',nowselecttable)
            us.commit()
            NextOrExit()
def Updata(cursor,tablename,us):
    while True:
        user =input('輸入0查詢當前數據,輸入1更新當前數據,任意輸入表示離開:')
        if user=='0':
            cursor.execute('SELECT * FROM ' + tablename + ";")
            nowselecttable = cursor.fetchall();
            print('表:',nowselecttable)
        elif user=='1':
            cursor.execute('SELECT * FROM ' + tablename + ";")
            nowselecttable = cursor.fetchall();
            print('表:', nowselecttable)
            idselect = input('輸入欲更改對象的id:')
            cursor.execute('SELECT *FROM '+tablename+" "+"WHERE id ="+idselect)
            datas=cursor.fetchall()
            print(datas)
            if len(datas)>0:
                while True:
                    off= input('繼續修改請輸入1,任意輸入離開')
                    if off=='1':
                        modify=input('輸入1修改(姓),2(名),3(年齡)4(性別)5(資產)')
                        if modify=='1':
                            firstname = '"'+input('欲替換姓')+'"'
                            cursor.execute('UPDATE '+tablename+" SET firstname="+firstname+' where id='+idselect+';')
                            print('修改成功')
                        if modify=='2':
                            lastname = '"'+input('欲替換名')+'"'
                            cursor.execute('UPDATE '+tablename+" SET lastname="+lastname+' where id='+idselect+';')
                            print('修改成功')
                        if modify == '3':
                            age = input('欲替換年齡')
                            cursor.execute(
                                'UPDATE ' + tablename + " SET age=" + age + ' where id=' + idselect + ';')
                            print('修改成功')
                        if modify == '4':
                            sex = input('欲替換性別M或F')
                            if sex != 'M' and sex!='F':
                                print('輸入錯誤')
                                continue
                            sex='"'+sex+'"'
                            print(sex)
                            cursor.execute(
                                'UPDATE ' + tablename + " SET sex=" + sex + ' where id=' + idselect + ';')
                            print('修改成功')
                        if modify=='5':
                            assets = input('欲替資產')
                            cursor.execute('UPDATE '+tablename+" SET assets="+assets+' where id='+idselect+';')
                            print('修改成功')
                        else:
                            print('輸入錯誤,請輸入欲修改對象的代號')
                            pass
                    else:
                        print('離開')
                        break
                cursor.execute('SELECT *FROM ' + tablename + " " + "WHERE id =" + idselect)
                datas = cursor.fetchall()
                print('更改後:',datas)
            elif len(datas)==0:
                print('不存在此id請重新輸入')
        else:
            us.commit()
            print('離開')
            NextOrExit()

def NextOrExit():
    while True:
        chooise=input('輸入1新增資料,輸入2更改資料,任意輸入離開')
        if chooise=='1' or chooise=='2':
            state = State()
            CreateTable(state[0], state[1], state[2])
            if chooise=='1':
                InsertValues(state[0], state[1],state[3])
            elif chooise=='2':
                Updata(state[0], state[1],state[3])
            else:
                print('離開')
                state[3].commit()
                # 關閉游摽然後關閉系統
                state[0].close()
                state[3].close()
                NextOrExit()
        else:
            print('離開')
            os._exit(0)


if __name__ == '__main__':
    import os
    NextOrExit()
