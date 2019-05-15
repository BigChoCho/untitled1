import tkinter
import ModTkinter
#登入
def reg():

    try:
        print(dict1.items())
        if e1.get() in dict1:
            lb3["text"] =("正確的用戶")
            print(dict1[e1.get()])
            if e2.get() ==dict1[e1.get()]:
                lb3["text"] = "登入成功"
                #調用自定義模塊
                ModTkinter.MODtkinter()
            else:
                lb3["text"] =("正確的用戶但密碼錯誤")
                #自動清除(可用len)
                e1.delete(0, 100)
                e2.delete(0, 100)
        else:
            lb3["text"] =("找不到該用戶")
            e1.delete(0, 100)
            e2.delete(0, 100)
    except NameError:
        lb3["text"] =("尚未註冊用戶,請先至少註冊一組")
    # name= e1.get()
    # pwd=e2.get()
    # if name=="111" and pwd =="222":
    #     lb3["text"] = "登入成功"
    # else:
    #     lb3["text"]="登入失敗"
#註冊
def rsd():
    try:
        if e1.get() not in dict1 and e2.get() not in dict1[e1.get()]:
            dict1.setdefault(e1.get(), e2.get())
            print(e1.get())
            print(dict1[e1.get()])
            lb3["text"] = ("註冊成功")
        else:
            lb3["text"] = ("重複或者無效的帳戶密碼")

    except KeyError:
        dict1.setdefault(e1.get(), e2.get())
        print(e1.get())
        print(dict1[e1.get()])
        lb3["text"] = ("註冊成功")
    else:
        lb3["text"] = ("重複或者無效的帳戶密碼")


#初始化準備
global dict1
dict1 = {}
#視窗
baseFrame = tkinter.Tk()
#名
lb1 = tkinter.Label(baseFrame,text="用戶名")
lb1.grid(row= 0,column=0,stick = tkinter.W)
#框
e1 = tkinter.Entry(baseFrame)
e1.grid(row=0,column = 1,stick=tkinter.E)

lb2 = tkinter.Label(baseFrame,text="密碼")
lb2.grid(row= 1,column=0,stick = tkinter.W)
e2 = tkinter.Entry(baseFrame)
e2.grid(row=1,column = 1,stick=tkinter.E)
#黨密碼用
e2["show"]='!'
#按鈕
btn = tkinter.Button(baseFrame,text="登入",command = reg)
btn.grid(row=2,column=1,stick=tkinter.E)
btn2 = tkinter.Button(baseFrame,text="註冊",command = rsd)
btn2.grid(row=2,column=0,stick=tkinter.E)
#驗證反映
lb3 = tkinter.Label(baseFrame,text="")
lb3.grid(row=3)


baseFrame.mainloop()