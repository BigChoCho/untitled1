#猜密碼小遊戲
import tkinter as tk
wimdow = tk.Tk()

def check_password():
    #初始化密碼
    password = "123448"
    entered_password =passwordEntry.get()
    if password == entered_password:
        confirmLabel.config(text = "正解")
    elif entered_password in password :
        confirmLabel.config(text= "接近")
    else:
        confirmLabel.config(text="大錯特錯DONKEY")
passwordLabel = tk.Label(wimdow,text = "你猜猜")
passwordLabel.pack()
confirmLabel = tk.Label(wimdow)
confirmLabel.pack()
passwordEntry = tk.Entry(wimdow,text="*")
passwordEntry.pack()
button = tk.Button(wimdow,text = "提交",command=check_password)
button.pack()
wimdow.mainloop()