#查找文件路徑(模糊搜尋) in 跟 == 的分別
#in 判斷是否在誰的裡面or疊代用or 字串中是否有相符如 "a" in "ab"
import os

star_dir = input("輸入目錄")
target = input("輸入文件名")
backup = []

def search_file(star_dir,target):
    os.chdir(star_dir)#切換用戶輸入的路徑

    for eacg_file in os.listdir(os.curdir):#當前文件夾
        if  target in eacg_file:
            #當前目錄的路徑+文件名
            backup_file = os.getcwd()+os.sep+eacg_file
            backup.append(backup_file)
        #如果是文件夾
        if os.path.isdir(eacg_file):
            search_file(eacg_file,target)
            #遞歸找完文件後退回上級目錄
            os.chdir(os.pardir)
    return backup


rd =search_file(star_dir,target)
print(rd)
#(當前路徑+\+自創文件名,)
f = open(os.getcwd()+os.sep+"backup.txt","w")
f.write("\n".join(rd))
f.close()