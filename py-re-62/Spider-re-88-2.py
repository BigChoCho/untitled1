import csv

#讀取或寫入csv檔,以分隔符判斷
#以表格方式 運用excle可打開


headers = ['ID','UserName','Age','Country']

rows = [
    (1000,'winco',100,'kho'),
    (1222,'dog',22,'doghos'),
    (2223,'obo',25,'das')
]

with open('spider_88_2.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    #寫入多行
    f_csv.writerows(rows)