file_name = input("文件名")
rep_word = input("請輸入欲替換字符")
new_word = input("欲替換新字符")
def file_replace(file_name,rep_word,new_word):
    f = open(file_name)
    content=[]
    for each in f:
        if rep_word in each:
            #替換字符串
            each = each.replace(rep_word,new_word)
            print("rrr",each)
        content.append(each)
    print(content)
    decide = input("YES/NO")
    if decide in ["YES","Yes","yes"]:
        f_write = open(file_name,"w")
        #重新依序寫入
        f_write.write("".join(content))
        f_write.close()
file_replace(file_name,rep_word,new_word)