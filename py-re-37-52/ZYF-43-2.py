Fname = input("文件名")
num_name = input("在第幾行格式 : ")

def file_view(Fname,num_name):
#split 分隔法

    f = open(Fname)

    begin,end = num_name.split(":")
    if begin =="":
        begin="1"
    if end =="":
        end = "-1"
    begin = int(begin)-1
    end = int(end)
    lines = end - begin
        #消耗begin前的幾行
    for i in range (begin):
        f.readline()
    if 0> lines:
        #打印全部
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline())

    f.close()
file_view(Fname,num_name)
