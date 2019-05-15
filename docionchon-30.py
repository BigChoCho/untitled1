from multiprocessing import Process
import os

def info(tit):
    print(tit)
    print("進程名",__name__)
    print("父進程",os.getppid())
    print("本身進程",os.getpid())

def f(name):
    info("function")
    print("helo",name)
def c ():
    info("ccc")

if __name__ == "__main__":
    info("main line")
    #子進程
    p = Process(target=f,args=("bob",))
    d = Process(target=c)
    p.start()
    p.join()
    d.start()
    d.join()

