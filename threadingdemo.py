## python多线程实战
## 什么是多线程?
'''
多线程类似于同时执行多个不同程序，多线程运行有如下优点：
> * 使用线程可以把占据长时间的程序中的任务放到后台去处理。
> * 用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
> * 程序的运行速度可能加快
> * 在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。

'''

import threading
import time

def sing(num):
    for i in range(num):
        print('sing%d'%i)
        time.sleep(.5)

def dance(num):
    for i in range(num):
        print('dance%d'%i)
        time.sleep(.5)

def multiThread():
    t_sing = threading.Thread(target=sing,args=(5,))
    t_dance = threading.Thread(target=dance,args=(6,))
    t1 = time.time()
    t_sing.start()
    t_dance.start()
    t2 = time.time()
    t_sing.join()  #等待线程终止
    t_dance.join() #等待线程终止
    print('多线程花费运行花费的时间是%fs'%((t2-t1))) 

def singleThread(): #单线程执行任务花的时间
    t1 = time.time()
    sing(5)
    dance(6)
    t2 = time.time()
    print('单线程花费运行花费的时间是%fs'%((t2-t1))) 
def main():
    multiThread()
    singleThread()

if __name__ == "__main__":
    main()
    
    