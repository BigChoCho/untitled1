import asyncio
import threading

async def sum(a,b):
    #返回當前對象
    print("now cal is {}".format(threading.currentThread()))
    r = int(a)+int(b)
    await asyncio.sleep(3)
    print("困辣{}".format(threading.currentThread()))
    return r
##建立一個Event Loop
loop = asyncio.get_event_loop()
task =asyncio.gather(sum(1,2),sum(2,3))
loop.run_until_complete(task)
r1,r2 = task.result()
print(int(r1)*int(r2))
loop.close()