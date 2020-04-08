'''
@Author: kingw
@Date: 2020-03-12 11:45:31
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
        print(f'call {f.__name__} in {t2-t1}s')
        return s
    return fn

def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
#装饰器就相当于在函数调用之前套用一个函数
newfn = performace(factorial)
print(newfn(10))

