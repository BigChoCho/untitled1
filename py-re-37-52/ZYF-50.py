import asyncio

movie_list = ["兵學奇緣.mp4","紙牌屋.avi","淫亂學員.rmvb","三國.mp4"]
music_list = ["幹.mp3","睡前音樂.mp3"]
movie_format = ["mp4","avi"]
music_format = ["mp3"]

# @asyncio.coroutine
async def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("收看:{}".format(i))
            #yield類似return但不中斷程序
            await asyncio.sleep(1)
        elif i.split(".")[1] in music_format:
            print("收聽:{}".format(i))
            await asyncio.sleep(2)

        else:
            print("沒有播放的格式")
loop = asyncio.get_event_loop()
task = [play(movie_list),play(music_list) ]
loop.run_until_complete(asyncio.wait(task))