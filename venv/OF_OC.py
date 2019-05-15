import tkinter
def base():

    C = int(en1.get())
    F = C * (9 / 5) + 32
    F = str(F)
    print(F)
    #顯示答案
    lb = tkinter.Label(baseFrame, text="°F="+F)
    #答案位置
    lb.grid(row=4,column=1)
    return;
def base2():
    F = int(en2.get())
    C = (F - 32) * (5 / 9)
    C = str(C)
    print(C)
    # 顯示答案
    lb = tkinter.Label(baseFrame, text="°C=" + C)
    # 答案位置
    lb.grid(row=4, column=1)
    return




def baseLabel(event):
    global baseFrame
    global en1
    baseFrame = tkinter.Tk()
    #定義名稱
    lb1 = tkinter.Label(baseFrame,text = "輸入°C")
    #定義位置
    lb1.grid(row=0,sticky = tkinter.W)
    #定義框
    en1 = tkinter.Entry(baseFrame)
    #定義框位
    en1.grid(row=0,column =1 ,sticky=tkinter.E)
    #傳輸鍵
    tkinter.Button(baseFrame, text='Show', command=base).grid(row=3, column=1, sticky=tkinter.W, pady=4)
def baseLabe2(event):
    global baseFrame
    global en2
    baseFrame = tkinter.Tk()
    lb1 = tkinter.Label(baseFrame, text="輸入°F")
    lb1.grid(row=0, sticky=tkinter.W)
    en2 = tkinter.Entry(baseFrame)
    en2.grid(row=0, column=1, sticky=tkinter.E)
    tkinter.Button(baseFrame, text='Show', command=base2).grid(row=3, column=1, sticky=tkinter.W, pady=4)
#父控件(主視窗)
baseFrame = tkinter.Tk()
#按鈕文字
lb = tkinter.Label(baseFrame, text="°C =°F, 輸入°C")
#按鈕導向
lb.bind("<Button-1>", baseLabel)
#自動布局位置
lb.pack()
lb2 = tkinter.Label(baseFrame, text="°F =°C, 輸入°F")
lb2.bind("<Button-1>", baseLabe2)
lb2.pack()
baseFrame.mainloop()