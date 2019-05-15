#隨機名子TKINTER
import tkinter as tk
import random
window =tk.Tk()
def random_1():
    s1 = ["case","happy","dog"]
    s = random.choice(s1)
    return s
def random_2():
    s2 = ["ead","food","look"]
    s =random.choice(s2)
    return s
def button_click():
    #獲取用戶輸入資訊
    name = nameEntry.get()
    verb = random_1()
    noun = random_2()
    sentence = name +""+verb+""+noun
    #刪除結果框的內容frist,end
    result.delete(0,tk.END)
    #生成默認內容
    result.insert(0,sentence)
#標題
nameLabel = tk.Label(window,text="name")
#輸入框
nameEntry = tk.Entry(window)
#按鈕
button  = tk.Button(window,text="生成隨機",command = button_click)
#結果框
result=tk.Entry(window)

nameLabel.pack()
nameEntry.pack()
button.pack()
result.pack()

window.mainloop()
