'''
@Author: kingw
@Date: 2020-03-12 12:04:16
@Description: file content
'''
#python的高阶函数之装饰器模式
#定义一个zhuang
import time
from functools import reduce
def performace(f):
    print(f.__name__)
    def fn(*args,**kw):
        t1 = time.time()
        s = f(*args,**kw)
        t2 = time.time()
        print(t2,t1,s)
        print(f'call {f.__name__} in {t2-t1}s')
        return s
    return fn
@performace
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
#装饰器就相当于在函数调用之前套用一个函数

print(factorial(10000))
'''
def wrap(f):
    #这个参数是怎么传递的，我嚓，我怎么有点看不懂呢
    def fn(*args,**kw):
        return f(*args,**kw)
    return fn
def myfn(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
#为什么要这样写呢
print(wrap(myfn)(10000))
'''