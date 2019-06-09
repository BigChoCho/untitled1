# 整理得有點亂,多多包涵囉~~~
def MYSQL(rows):
    import pymysql

    # 注意下面mysql與法中的空格別亂刪!會報錯的!!

    # 欲創建的數據庫名稱
    dataname = 'spider'
    # 創建數據庫指令默認utf-8
    createdata = 'CREATE DATABASE ' + dataname
    # print(createdata)
    # 判斷是否存在數據庫開關聲明
    dataif = False
    tablif = False
    # _______
    # 創建的數據表名稱
    tablename = 'spider_90'
    # 建立數據表中數據及創建聲明
    createtable = 'CREATE TABLE ' + tablename + '(tit VARCHAR(32),text TEXT,href TEXT,date VARCHAR(32);'
    # print(createtable)

    # _________________以上是聲明變量待會要用!____________
    # 本地ip對超級用戶進行操作,置於你要遠端訪問的話,需要設置防火牆,跟文件配置,授權等...自己上網找吧@@....
    db = pymysql.connect('127.0.0.1', 'root', "111")
    print(db)
    # 創見游標對數據進行操作
    cursor = db.cursor()
    # MYSQL中查找所有數據庫
    cursor.execute('SHOW DATABASES')
    # 接收所有數據
    datas = cursor.fetchall()

    for data in datas:
        # 因為這傢伙是tuple類型所以需要用index的方式將它取出
        # 一但找到了表示不需要創建
        if data[0] == dataname:
            print('已存在', data[0])
            dataif = True
            break
        # 如果不存在便進行創建
    if dataif == False:
        cursor.execute(createdata)
        # 提交
        db.commit()
    # 進入該數據庫
    cursor.execute('USE ' + dataname)
    # 查找所有數據表
    cursor.execute('SHOW TABLES')
    # 接收所有數據
    datas = cursor.fetchall()
    # 創建數據表及判斷表是否存在如不存在創建!
    for data in datas:
        if data[0] == tablename:
            print('已存在', data[0])
            tablif = True
            break
    if tablif == False:
        cursor.execute(createtable)
        # 提交
        db.commit()
        print('創建成功')
    # 先清空殘餘數據
    cursor.execute('DELETE FROM ' + tablename)
    db.commit()
    for row in rows:
        cursor.execute('INSERT INTO ' + tablename + ' VALUE ' + row + ';')
    db.commit()
    print('over')
    cursor.close()  # 關閉游標
    db.close()  # 關閉數據庫


def Spider():
    # 懶地註釋囉!自己查吧
    import requests
    from lxml import etree
    import re
    # 模擬請求頭
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36"
    }
    # 抓取網址，請求頭
    r = requests.get('http://www.seputu.com/', headers=headers)

    html = etree.HTML(r.text)
    rows = []
    titall = html.xpath('//*[@class="mulu"]')
    for tit in titall:
        h2 = tit.xpath('.//div[@class="mulu-title"]/center/h2/text()')
        # 判斷是否存在內容
        if len(h2):
            h2tit = h2
            a_s = tit.xpath('./div[@class="box"]/ul/li/a')
            for a in a_s:
                href = a.xpath('./@href')[0]
                tits = a.xpath('./@title')[0]
                # 匹配所有
                pattern = re.compile(r'\s*\[(.*)]\s+(.*)')
                match = pattern.search(tits)
                if match != None:
                    data = match.group(1)
                    real_title = match.group(2)
                    content = (h2tit[0], real_title, href, data)
                    # 這邊之所以轉str是因為它是tuple類型不利於接下來的操作
                    rows.append(str(content))
    return rows


if __name__ == '__main__':
    rows = Spider()
    MYSQL(rows)