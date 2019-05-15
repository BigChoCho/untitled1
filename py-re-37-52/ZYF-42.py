Fname = input("用戶名")
def FFname(Fname):
    f = open(Fname,"w")
    print("輸入內容,輸入:w = 保存退出")

    while True:
        W = input()
        #判斷用戶是否輸入w
        if W != ":w":
            #不等於的請況下輸入內容
            #(字串,換行
            f.write("%s\n" % W)
        else:
            break
    f.close()
FFname(Fname)


