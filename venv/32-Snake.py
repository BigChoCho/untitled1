import tkinter
import queue
import threading
import time
import random

class World(threading.Thread):
   def __init__(self):
        threading.Thread.__init__(self)


        print("sss1")
        self.queue = q
        self.is_game_over =False
        self.root = tkinter.Tk()
        #畫布
        self.canvas = tkinter.Canvas(self.root,width = 800,height=600,bg="#00FF7F")
        self.canvas.pack()

        #畫出蛇
        self.snake = self.canvas.create_line((10, 10), (30, 10), fill="black", width=10)
        #食物方形
        self.food = self.canvas.create_rectangle(250,300,255,305,fill="black",outline="black")
        #記分板
        self.points_earned = self.canvas.create_text(450,20,fill="white",text="RASS")
        self.start()
        count = 0

        #避免按鍵偵測不到我的字串,先讓他判定為0並且給予賦值避免報錯
        Snake.key_pressed(self,count)
        #當觸發鍵盤任一符號(只能傳一次,接下來按多次都沒管用)
        self.root.bind('<Key>', lambda event: Snake.key_pressed(event,count+1))
        #啟動函數,並且傳入參數,啟動線程
        Snake(World, q, self.is_game_over,self.root)
        self.queue_handler()


        # self.root.mainloop()

   def queue_handler(self):
        #死循環不斷獲取
        #這邊如果不用block=False,程序會卡死,因為隊列已經被拿光了但程序扔然不斷的等待
        try:


             while True:
                  #block=False意味著不等待資源直接拋出異常(為非阻塞)
                  task = self.queue.get(block=False)
                  if task.get("game_over"):
                       self.game_over()
                  if task.get("move"):
                       points =[x for point in task["move"] for x in point]
                       print("我拿到了",points)
                       # *當隊列獲取move,重畫蛇的位置
                       self.canvas.coords(self.snake,*points)
                  if task.get("food"):
                       points1 = [x for point in task["food"] for x in point]
                       print("我拿到了食物",points1)



                       self.canvas.coords(self.food,*points1)

                       print("AND",points1)
        except queue.Empty:
             if not self.is_game_over:
                  #異常發生後,如果遊戲非結束,則在1秒後重新啟用
                  self.canvas.after(100,self.queue_handler)
   def game_over(self):

        #遊戲結束與按鍵彈出遊戲重置OR結束
        #一旦遊戲觸發結束將條件返回真
        print("促發惹game_over")
        self.is_game_over = True
        self.canvas.create_text(250,150,text="Game Over")
        # qb = Button(self, text="Quit", command=self.destroy)
        # rb = Button(self, text="Again", command=self.__init__)


class Snake(threading.Thread):
     def __init__(self,world,queue,is_game_over,root):
          threading.Thread.__init__(self)


          print("s2線程啟動")
          #傳入類
          self.world = world
          #傳入隊列
          self.queue= queue
          #預設值避免出錯(判斷當前按鍵用)
          # dierection = "UUP"
          # self.key_pressed()

          #遊戲結束判斷條件
          self.is_game_over = is_game_over
          #遊戲分數
          self.points_earned = 0
          #創建,並且將該隊列傳入食物類的對列
          self.food = Food(self.queue)
          #蛇的移動座標
          self.snake_points = [(495, 55), (485, 55), (465, 55), (455, 55)]
          #開啟線程
          print("啟動現成", time.ctime())
          self.start()

     #線程啟用後調用開函數
     def run(self,):

          print("run被調用了",time.ctime())
          if self.is_game_over:
               self.world.canvas.delete()
          #如果遊戲沒有結束,則不斷存放消息,並調用移動
          while not self.is_game_over:
               #不斷存放
               self.queue.put({"move": self.snake_points})
               time.sleep(0.3)

               #????????????????????????????????

               self.move()


     def move(self):
          #獲取調用函數的返回值,按鍵移動時重新計算
          print("MOV起來")

          self.new_snake_point = self.cal_new_position()
          print("食物",self.food.positon)
          print("蛇",self.cal_new_position)
          #如果蛇的當前座標與食物相疊
          if self.food.positon[0] == self.new_snake_point or  self.food.positon[1] == self.new_snake_point:
               self.points_earned+=1#得分
              #分數存入隊列
               self.queue.put({"points_earned":self.points_earned})
              #重新產生食物
               self.food.new_food()
          else:
               # 每次移动是删除存放蛇的最前位置，
               self.snake_points.pop(0)
          # 判断程序是否退出，因为新的蛇可能撞墙
               self.check_game_over(self.new_snake_point)
               #并在后面追加
               self.snake_points.append(self.new_snake_point)
     def cal_new_position(self):


          #重新計算蛇頭位置
          #倒數第一位
          print("try開始")
          print("cal_new_position起來")


          last_x,last_y = self.snake_points[-1]
          #判斷鍵位,返回座標
          if Snake.dierection == "Up":
               print("up直促發")

               self.new_snake_point=  last_x,last_y -10
          elif Snake.dierection == "Down":
               print("do直促發")
               self.new_snake_point=  last_x,last_y +10
          elif Snake.dierection == "Left":
               print("le直促發")
               self.new_snake_point=  last_x-10,last_y
          elif Snake.dierection == "Right":
               print("ri直促發")
               self.new_snake_point=  last_x+10,last_y
          else:
               Snake.new_snake_point = last_x,last_y
          print("有沒有搞錯啊",Snake.dierection)



          return  self.new_snake_point


     def key_pressed(self,count):
          print("key_pppppp")
          #爛東西,總是不給我傳參只好搞下做(按下按鍵給我+1,但絲乎只能傳一次接下來按下去就沒法傳了)
          self.count = count
          if self.count <=0 :
               Snake.dierection ="Left"

               print("count=",count)
          else:
               Snake.dierection =self.keysym
               #獲取當前鍵盤符號str呈現
               print("key_pressed")
               print("key",Snake.dierection)
               # self.dierection = self.keysym
               #?????????????????????????????????????????????


          # print(self.dierection)
    #判斷蛇是否撞牆
     def check_game_over(self,snake_point):
          #在元組中抽出x,y
          x,y =self.snake_points[0]
          print(x,y)
          #如果超過邊寬或是咬到自己(咬到自己還沒做判斷?)
          if not -5<x<805 or not -5<y<605 :
               print("您是超過範圍嗎")
               self.queue.put({"game_over":True})
class Food():
     def __init__(self,queue):
          self.queue =queue

          self.new_food()
     def new_food(self):
          #可被10整除的隨機範圍



          x = random.randrange(50,480,10)
          #由於方塊必須有4個值
          x1 =x+5
          y = random.randrange(50,480,10)
          y1 =y+5
          #放座標用,放入list才可以迭代
          self.positon = [(x,y),(x1,y1)]
         #放入隊列(頭out,尾put)
          self.queue.put({"food":self.positon})





q = queue.Queue()
world=World()

world.root.mainloop()

