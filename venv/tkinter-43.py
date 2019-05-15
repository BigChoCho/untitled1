import random
import tkinter
#定義球
class Randomball():
    #傳入畫布以及畫布的寬高
    def __init__(self,canvas,scrnwidth,scrnheight):
        #球出現的初始位置隨機,上限,下限=屏寬-20
        #球卡在框框的問題在於球的座標再加上radius後會超出屏幕所以只要限制他的範圍不高出,例如:(下面的120)
        #X座標
        self.xpos=random.randint(50,int(scrnwidth-120))
        #y座標
        self.ypos = random.randint(50,int(scrnheight-120))
        #球速
        self.xvelocity = random.randint(1,3)
        self.yvelocity = random.randint(1, 3)
        #定義屏寬,限制位置
        #寬
        self.scrnwidth =scrnwidth
        #高
        self.scrnheight =scrnheight
        #球大小也隨機
        self.radius = random.randint(20,120)
        #定義一個快速且匿名而且隨機的函數(每一次被調用數值得以不同)
        #RGB255球色
        c=lambda :random.randint(0,255)
        self.color = "#%02x%02x%02x"%(c(),c(),c())
        self.canvas =canvas
    def create_ball(self):
        #已知圓心的X剪去半徑得出初始位置
        x1 = self.xpos - self.radius
        x2 = self.xpos+self.radius
        y1 = self.ypos-self.radius
        y2 = self.ypos+self.radius
        #在畫布畫個正圓
        #outline 外圍顏色
        self.item = self.canvas.create_oval(x1, y1,x2, y2, fill=self.color,outline=self.color)

    def move_ball(self,):
        #改變球的座標
        self.xpos+=self.xvelocity
        self.ypos+=self.yvelocity
        # print("x:"+str(self.xpos))
        # print("y"+str(self.ypos))
        #球的碰撞反映
        if self.xpos+self.radius>=self.scrnwidth or self.xpos-self.radius<=0:
            self.xvelocity*=-1
        if self.ypos+self.radius>=self.scrnheight or self.ypos-self.radius<=0:
            self.yvelocity*=-1
        #球移動速度
        self.canvas.move(self.item,self.xvelocity,self.yvelocity)

#定義屏幕保護
class ScreenSaver():




    balls =list()
    def __init__(self):




        #啟動球的數量(隨機)
        self.num_balls = random.randint(6,20)
        # self.num_balls = 1
        self.root = tkinter.Tk()



        #取消框
        self.root.overrideredirect(1)
        #屬標移動退出
        # self.root.bind("<Motion>",self.myquit)
        #獲取主視窗的長寬
        w,h = self.root.winfo_screenmmwidth()+500,self.root.winfo_screenheight()
        #決定畫布的大小
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        #布局
        self.canvas.pack()
        #畫球跟隨機數量

        for i in range(self.num_balls):
            #實例化傳入畫布跟值
            ball =Randomball(self.canvas,scrnwidth=w,scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_scree()
        self.Buttonmenu()

        self.root.mainloop()


    def run_scree(self):
        for ball in self.balls:
            #動起來
            ball.move_ball()

        #200毫秒啟動一個函數
        self.canvas.after(2,self.run_scree)
    def Buttonmenu(self):
        def pop(self):
            outmenu.post(self.x_root, self.y_root)

        #退出功能
        myquit =lambda:self.root.destroy()

        # 滑鼠右鍵彈出菜單+刷新以及退出功能
        outmenu = tkinter.Menu(self.root)
        outmenu.add_command(label="跳出", command=myquit)

        self.root.bind("<Button-3>", pop)



if __name__ == "__main__":


    ScreenSaver()



