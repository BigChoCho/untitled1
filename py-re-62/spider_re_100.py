
# http://m801.music.126.net/20190611134453/57c407e75f3995a39bdfa700e87672c5/jdyyaac/5153/0e5d/565f/f9b40b31509708491f05a5a230727ec8.m4a
# https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=
# /song?id=34923289
#http://musci.163.com/song/media/outer/url?id=502238497.m4a

from tkinter import *
from tkinter.filedialog import askdirectory


from PIL import ImageTk
import os
import requests
from lxml import etree
class Spider(object):

    def __init__(self):
        self.headers = {

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
        }

    def Main(self,info,listbox):
        global net
        count = 0
        dicts = {}
        def CallOn(event):
            global net2
            if net2==False:
                key=listbox.get(listbox.curselection())
                if key in dicts:
                    spider.Main2(dicts[key])
        url = "https://www.ximalaya.com/search/"+info
        html = requests.get(url, headers=self.headers).text
        datas =etree.HTML(html)
        titls=datas.xpath("//a[@class='xm-album-title ellipsis-2']/div/text()")
        hrefs = datas.xpath("//a[@class='xm-album-title ellipsis-2']/@href")
        for tit,href in zip(titls,hrefs):
            dicts[tit] =href
            count+=1
        for name in dicts:
            listbox.insert(count,(name))

        listbox.bind('<Double-Button-1>',CallOn)
    def Main2(self,values):
        import re
        values=values.split('/')[-2]
        url ="https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=1&pageSize=30".format(values)
        json = requests.get(url,headers=self.headers).text
        trackName = re.findall(r'"trackName":(.*?),', json)
        src = re.findall(r'"src":(.*?),', json)
        tkinters.Windows(trackName,src)




class Tkinter(object):

    def __init__(self):
        self.root = Tk()
        self.root.title('專屬音樂盒')
        #窗口大小
        self.root.geometry('900x700')
        #窗口位置
        self.root.geometry('+1000+280')
    def Set(self):
        #滾定條
        scrollbar =Scrollbar(self.root,orient='horizontal')
        scrollbar.grid(row=2, column=0,sticky='ew')
        #font大小,字體
        lable = Label(self.root,text="查找歌手,或歌名:",font=('標楷體',20))
        #布局默認行列(0,0)
        lable.grid(row=0,sticky=E)
        #內容被獲取用
        # lastring = tk.StringVar()
        #輸入框 width=框的寬度
        entry = Entry(self.root,font=(13),width=40)
        entry.grid(row=0,column=1,sticky=E)
        # 列表框
        listbox = Listbox(self.root, font=('標楷體', 15), width=60, height=25)
        listbox.grid(row=1, columnspan=2)
        listbox.configure(xscrollcommand=scrollbar.set)
        # 發送按鈕
        outside = Button(text="宏哥快搜",font=('標楷體',13),width=10,command= lambda:GetInfo(entry,listbox))
        outside.grid(row=0,column=2)
        scrollbar.configure(command=listbox.xview)
        self.root.mainloop()
    def Windows(self,trackName,src):

        def CallOn(event):
            global net2
            global off
            global off2
            print(off)
            if net2 == False:
                name = listbox.get(listbox.curselection())
                if '"'+name+'"' in trackName:
                    index=trackName.index('"'+name+'"')
                    if src[index]=='null':
                        listbox2.insert(END,'這連結爆了換別的吧')
                    elif off==True and off2==True:
                        listbox2.insert(END, name + '下載中,請稍後....')
                        listbox2.see(END)
                        listbox2.update()
                        href =src[index]
                        Downlod(name,href,getpath(),listbox2)
                    else:
                        root = Tk()
                        root.geometry('+1250+480')
                        Label(root, text="尚未設置路徑,請先設置!!").grid(row=0, column=0)

        def selectPath():
            global off2
            path_ = askdirectory()
            path.set(path_)
            print(path)
            off2 = True
        def getpath():
            global off
            paths = path.get()
            Label(root2, text=paths).grid(row=1, column=3)
            off =True
            return paths
        global off,off2
        off = False
        off2 =False
        count =0
        root2 =Tk()
        root2.title('下載視窗')
        # 窗口大小
        root2.geometry('1200x700')
        # 窗口位置
        root2.geometry('+950+280')
        lable = Label(root2, text="點擊音樂下載:", font=('標楷體', 20))
        # 布局默認行列(0,0)
        lable.grid(row=0, sticky=E)
        listbox = Listbox(root2, font=('標楷體', 15), width=55, height=25)
        listbox.grid(row=1, column=0)
        listbox2 = Listbox(root2, font=('標楷體', 15), width=40, height=25)
        listbox2.grid(row=1, column=1)
        path = StringVar()
        Label(root2, text="目標路徑:").grid(row=1, column=2)
        print(path)
        Button(root2, text="下載路徑設置", command=selectPath).grid(row=0, column=2)
        Button(root2, text="確定", command=getpath).grid(row=0, column=3)
        for name in trackName:
            count+=1
            listbox.insert(count,name.strip('"'))
        listbox.bind('<Double-Button-1>', CallOn)


def GetInfo(entry,listbox):
    # 判斷結束爬蟲後才被執行
    if net == False:
        info = entry.get()
        spider.Main(info,listbox)
def Downlod(name,href,path,listbox2):
    print(href,path)

    music = requests.get(href.strip('"'), headers=spider.headers)
    with open(path + "\\" + name.strip() + '.m4a', 'wb')as f:
        f.write(music.content)
        listbox2.insert(END, '下載完畢...')

if __name__ =="__main__":
    net =False
    net2=False
    spider=Spider()
    tkinters=Tkinter()
    tkinters.Set()
