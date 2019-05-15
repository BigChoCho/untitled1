#行數是否相同
fill = input("frist1")
fill2 = input("frist2")

def fill_compare(fill,fill2):
    f1 = open(fill)
    f2 = open(fill2)
    #統計行數
    count= 0
    #統計不一樣數量
    differ= []
#遍歷文件內容
    for lill in f1:
        #以每行依序存入
        lill2 = f2.readline()
        count +=1
        if lill != lill2:
            #如果不同,標誌在第幾行數
            differ.append(count)
    f1.close()
    f2.close()
    return differ

differ = fill_compare(fill,fill2)
if len(differ) == 0 :
    print("文件內容完全相同")
else:
    print("總共有%d個不同"% len(differ))
    for i in differ:
        print("第%d不同"% i)
