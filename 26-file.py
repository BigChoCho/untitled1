# 第一步： 画出图形界面上部
from tkinter import *

root = Tk()
# 定义面板的大小
root.geometry('250x380')
root.title("北京图灵学院")

# 定义面板
# bg代表背景颜色（background）， #dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=300, height=150, bg='#dddddd')
frame_show.pack()

# 定义顶部区域
#不斷的偵測訊息
sv = StringVar()
sv.set('0')
global num1
global num2
global operator
num1 = ""
num2=""
operator=None
# anchor:定义控件的锚点，e代表右边
# font代表字体
#計算框
show_label = Label(frame_show, textvariable=sv, \
                  bg='green', width=12, height=1,\
                  font=("黑体", 20, 'bold'),\
                  justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)
def delete():
    print("我被删除了")


def fan():
    print("烦了")


def clear():

    print("科利尔")
def change(num):
    global num1
    global num2
    # 加入操作数是None，表明肯定是第一个操作数
    if not operator:
        num1 = num1 + num
        # 如果是第一个操作数，则只显示第一个操作数

        sv.set(num1)
    else:

        num2 = num2 + num

        # 如果是第二个操作数 ，则应该显示完整的计算式子
        sv.set(num1 + operator + num2)
    #加號
def operation(op):
    global operator
    if op in ['+', '-', 'x', '/']:
        operator = op
    else:  # 认为是按下( = )
        if op == "+":
            rst = int(num1) + int(num2)
        if op == "-":
            rst = int(num1) - int(num2)
        if op == "x":
            rst = int(num1) * int(num2)
        if op == "/":
            rst = int(num1) / int(num2)

        sv.set(str(rst))
# 按键区域
frame_bord = Frame(width=400, height=350, bg='#cccccc')
#開始定義按鈕#定義按鈕位置
b_del = Button(frame_bord, text="←", width=5, height=1, command=delete).grid(row = 0,column=0)
utton_clear = Button(frame_bord,text = 'C',width = 5,height =1,command = clear).grid(row = 0,column = 1)
#正負號
button_fan = Button(frame_bord,text = '±',width = 5,height =1,command = fan).grid(row = 0,column = 2)
button_ce = Button(frame_bord,text = 'CE',width = 5,height =1,command = clear).grid(row = 0,column = 3)
#數字按鍵部分,藉由中介函數傳入參數
b_1 = Button(frame_bord, text='1', width=5, height=2,command=lambda:change("1")).grid(row=1, column=1)
b_2 = Button(frame_bord, text='2', width=5, height=2,command=lambda:change("2")).grid(row=2, column=1)
b_3 = Button(frame_bord, text='3', width=5, height=2,command=lambda:change("3")).grid(row=3, column=1)
#+號
b_jia = Button(frame_bord, text='+', width=5, height=2,command=lambda:operation("+")).grid(row=1, column=0)
b_jia1 = Button(frame_bord, text='-', width=5, height=2,command=lambda:operation("-")).grid(row=2, column=0)
b_jia2 = Button(frame_bord, text='x', width=5, height=2,command=lambda:operation("x")).grid(row=3, column=0)
b_jia3 = Button(frame_bord, text='/', width=5, height=2,command=lambda:operation("/")).grid(row=4, column=0)



# b = []
#
# for i in range(1,4):
#     print(i)
#
#     b.append(Button(frame_bord,text=str(i),width=5,height=2,command=lambda:change(i)).grid(row=i+1,column=0))


#綁定區塊
frame_bord.pack(padx=10, pady=10)


root.mainloop()

