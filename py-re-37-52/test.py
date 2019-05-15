import os
#獲取當前文件夾下的所有文件
all_files = os.listdir(os.curdir)#當前目錄
print(all_files)
for i in all_files:
    if os.path.isdir(i):
        print("文夾",i)
