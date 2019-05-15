#猜隨機整數
import tkinter as tk
import random
wimdow = tk.Tk()
maxnum =10
#計分
score =0
#第幾回合
rounds=0
def check_password():
    global score
    global rounds
    try:
        guess = int(guessBox.get())
        print("dddd")
        if 0<guess<=maxnum:
            print("aaaa")
            result = random.randrange(1,maxnum+1)
            print("result",result)

            print("1")
            if guess == result:
                score+=1
                print("2",score)
            rounds +=1
            print("3",rounds)
        else:
            result="輸入錯誤"
    except:
        result="北七喔"
    print("4")
    #改動
    scoreLabel.config(text="當前分數{},當前回合{}".format(score,rounds))
    print("5")

    resultLable.config(text = "答案是"+str(result)+"請輸入1-10")
    guessBox.delete(0,tk.END)


resultLable = tk.Label(wimdow,text = "請輸入1-10")
scoreLabel = tk.Label(wimdow,text="當前分數{},當前回合{}".format(score,rounds))
guessBox = tk.Entry(wimdow)
button = tk.Button(wimdow,text = "提交",command=check_password)

resultLable.pack()
scoreLabel.pack()
guessBox.pack()
button.pack()

wimdow.mainloop()