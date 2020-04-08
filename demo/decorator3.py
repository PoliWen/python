'''
@Author: kingw
@Date: 2020-03-12 14:16:53
@Description: file content
'''
#装饰器传递参数
from functools import reduce
import time,functools
def performance(uni):
    def decorator(f):
        @functools.wraps(f) #通过这种方法把原有函数的所以必要属性都都一个个复制到新函数上
        def wraper(*args,**kw):
            t1 = time.time()
            s = f(*args,**kw)
            t2 = time.time()
            print(f'{f.__name__} call in {(t2-t1)} {uni}')
            return s
        return wraper
    return decorator
@performance('ms')
def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))
print(factorial(1000))
print(factorial.__name__)
