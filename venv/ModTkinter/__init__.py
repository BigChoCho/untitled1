def MODtkinter():
    import tkinter
    # 被工具列調用的方法
    def makeLabel():
        # 聲明全局主窗
        global bas
        # 顯示訊息,並且自動布局
        tkinter.Label(bas, text="進入工具欄").pack()
        # 鼠標位置,需要回傳的參數,post,是當前位置的x,y座標

    def pop(event):
        outmenu.post(event.x_root, event.y_root)

    # 聲明一個主視窗
    bas = tkinter.Tk()
    # 創建菜單連結主視窗
    menu = tkinter.Menu(bas)
    # 創建彈出式菜單連結主窗
    outmenu = tkinter.Menu(bas)
    # 依序添加點擊菜單
    for x in ["複製", "貼上", "剪裁"]:
        # 添加分割符
        outmenu.add_separator()
        # 依序添加點擊菜單
        outmenu.add_command(label=x)
    # 添加一個點擊菜單,並且使他在被點擊以後進入一個方法
    outmenu.add_command(label="工具列", command=makeLabel)

    # 創建菜單連結主菜單
    menu2 = tkinter.Menu(menu)
    menu3 = tkinter.Menu(menu)
    menu4 = tkinter.Menu(menu)
    # 依序添加菜單名
    # 副菜單
    for item in ['複製', '黏貼', '設定', '傳輸']:
        menu2.add_command(label=item)
    for item in ['存檔', '另存新檔', '新檔案', '開啟檔案']:
        menu3.add_command(label=item)
    for item in ['日期', '介紹', '地址', '安全協定']:
        menu4.add_command(label=item)
    # 主菜單
    menu.add_cascade(label="檔案", menu=menu3)
    menu.add_cascade(label="文件", menu=menu2)
    menu.add_cascade(label="關於", menu=menu4)
    # 右鍵副菜單
    outmenu.add_cascade(label="巨集", menu=menu2)
    bas["menu"] = menu
    # Button-3是滑鼠右鍵,並且點擊後啟用方法
    bas.bind("<Button-3>", pop)
    bas.mainloop()
if __name__ == '__main__':
    MODtkinter()