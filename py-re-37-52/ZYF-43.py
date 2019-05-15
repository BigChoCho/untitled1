Fname = input("文件名")
num_name = input("在第幾行格式")

def file_view(Fname,num_name):
    print("\n文件%s中的第%s行以前:"% (Fname,num_name))

    f = open(Fname)
    for i in range (int(num_name)):
        print(f.readline())
    f.close()
file_view(Fname,num_name)