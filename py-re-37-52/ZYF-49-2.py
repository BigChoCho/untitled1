#多進程
import multiprocessing
import threading
import time
movie_list = ["兵學奇緣.mp4","紙牌屋.avi","淫亂學員.rmvb","三國.mp4"]
music_list = ["幹.mp3","睡前音樂.mp3"]
movie_format = ["mp4","avi"]
music_format = ["mp3"]
def play(playlist):
    #判斷格式
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("收看:{}".format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("收聽:{}".format(i))
            time.sleep(2)
        else:
            print("沒有播放的格式")

class MyThread(threading.Thread):
    def __init__(self,playlist):
        super().__init__()
        self.playlist = playlist
    def run(self):
        play(self.playlist)
if __name__ == "__main__":
    t1=multiprocessing.Process(target=play,args=(movie_list,))
    t2=multiprocessing.Process(target=play,args=(music_list,))
    t1.start()
    t2.start()