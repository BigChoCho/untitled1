import os
import time
import json

count= 0
exit_flag = False
while count<3:
    user = input("輸入用戶名")
    #移除頭尾空格
    f = user.strip()+".json"
    #檢查檔案路徑是否存在
    if os.path.exists(f):
        print("存在")
        #開啟檔案(對象,權限,編譯)
        fp = open(f,"r+",encoding="utf-8")
        #轉譯json
        j_user = json.load(fp)

        if j_user["status"] == 1:
            print("帳號已鎖定")
            break
        else:
            #沒鎖定的話
            dt = j_user["expire_date"]
            #返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
            cst = time.time()
            #轉譯成1970纪元后经过的浮点秒数(轉譯年月日
            est = time.mktime(time.strptime(dt,"%Y-%m-%d"))
            print(est)
            #當前時間>用戶日期
            if cst>est:
                print("用戶已過期")
                break
            else:
                while count<3:
                    pwd = input("密碼")
                    if pwd.strip() == j_user["password"]:
                        print("登入成功")
                        exit_flag = True
                        break
                    else:
                        if count == 2:
                            print("用戶登入超過3次,鎖號")
                            j_user["status"] =1
                            #f.seek(偏移量,[起始位置])：用来移动文件指针。
                            fp.seek(0)
                            fp.truncate()#清空文件內容
                            #重新建立文件
                            json.dump(j_user,fp)

                    count +=1

    if exit_flag:
        print("運行節素")
        break
    else:
        print("用戶不存在")
        count +=1
