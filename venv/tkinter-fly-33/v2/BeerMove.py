import tkinter
import time
import random as rd

'''
蜜蜂从上向下运动
可以通过键盘左右控制
'''

step = 0#计数器，计算一共小飞机走了多少步
direciton = (1,1)
x=0
y=10

def set_right(e):
    global x
    x += 1
    print(x)

def set_left(e):
    global x
    x -= 1
    print(x)
def ap_move():
    global  step
    global x
    global  y
    #每次調用該函數,小飛機不斷向下20
    y += 0.000000000000000001
    print(x,y)
    #每次調用左右控制小飛機並且自動向下跑
    window_canvas.move("sp", x, y)
    #每次被調用一次計步器都會+1
    step +=1
    #每1秒調動一次
    window_canvas.after(100,ap_move)
    print("我走了",step,"次")
def main():
    #创建
    # 创建开始界面
    background_image_fullname =  r"..\img\background.gif"
    # background_image_fullname = "/home/augs/AirPlane/img/start.gif"
    # background_image_fullname = "start.gif"
    #實例介面
    start_img = tkinter.PhotoImage(file=background_image_fullname)
    #定義大小位置
    window_canvas.create_image(480 / 2, 600 / 2,anchor=tkinter.CENTER,image=start_img,tags="start")

    sp = r"..\img\smallplane.gif"
    sp_img = tkinter.PhotoImage(file=sp)
    window_canvas.create_image(50,100 / 2, anchor=tkinter.CENTER,image=sp_img,tags="sp")
    # 让小飞机动起来
    ap_move()
    tkinter.mainloop()

root_window = tkinter.Tk()
root_window.title("北京图灵学院")


root_window.bind('<Key-Left>', set_left)
root_window.bind('<Key-Right>', set_right)
#視窗鎖死
root_window.resizable(width=False, height=False)

#创建画布
window_canvas = tkinter.Canvas(root_window,width=480,height=600)
window_canvas.pack()
if __name__ == '__main__':
    main()