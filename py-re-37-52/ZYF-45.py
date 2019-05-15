#查找文件的路
import os

star_dir = input("輸入目錄")
target = input("輸入文件名")

def search_file(star_dir,target):
    os.chdir(star_dir)#切換用戶輸入的路徑

    for eacg_file in os.listdir(os.curdir):#當前文件夾
        if eacg_file == target:
            #當前目錄的路徑+文件名
            print(os.getcwd()+"\\"+eacg_file)
            print(os.getcwd())
            print(eacg_file)
        #如果是文件夾
        if os.path.isdir(eacg_file):
            search_file(eacg_file,target)
            #遞歸找完文件後退回上級目錄
            os.chdir(os.pardir)
search_file(star_dir,target)
