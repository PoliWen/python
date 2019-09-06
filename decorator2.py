#decorator python装饰器
#写一个判断函数运行性能的函数
#如何让decorator带参数传递
#闭包，跟装饰器还得好好学学
import time 
from functools import reduce
import functools
def performance(unit):
    def decorator(f):
        @functools.wraps(f)  #改变函数__name__,__doc__的指向的
        def wraper(*args,**kw):
            t1 = time.time()
            r = f(*args,**kw)
            t2 = time.time()
            t = (t2-t1)*1000 if unit == 'ms' else (t2-t1)
            print('call %s() in %f %s'%(f.__name__,t,unit))
            return r
        return wraper
    return decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial(10000))
print(factorial.__name__)
