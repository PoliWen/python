#decorator python装饰器
#写一个判断函数运行性能的函数
import time 
from functools import reduce
def performace(f):
    def fn(*args,**kwargs): #记着必须按照这种模式来写装饰器函数，返回一个函数
        t1 = time.time()
        r = f(*args,**kwargs)  #一秒都不要就可以计算完
        t2 = time.time()
        print('call %s() in %fs'%(f.__name__,(t2-t1)))  #10000的阶乘，算出来要五秒
        return r
    return fn
@performace
def factorial(n):
    r  = reduce(lambda x,y:x*y,range(1,n+1))
    return r
print(factorial(10000))  #haha,计算机哦，这个数就算不出来了
