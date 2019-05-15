import os
#獲取當前文件夾下的所有文件
all_files = os.listdir(os.curdir)#當前目錄
type_dict = dict()

for each_file in all_files:
    #判斷是否為文件夾
    if os.path.isdir(each_file):
        #設定名稱跟編號
        type_dict.setdefault("文件夾",0)
        type_dict["文件夾"]+=1
    else:
        ext = os.path.splitext(each_file)[1]#獲取文件名[0]表示文件名[1]檔案類型名
        print("sss",ext)
        type_dict.setdefault(ext,0)
        type_dict[ext]+=1
for each_type in type_dict:
    print("該文件夾下類型為{},的文件{}個".format(each_type,type_dict[each_type]))
