#python中map的使用
from functools import reduce #在python3中reduce函数被放放到了functools模块里面了
def fomatStr(s):
	return s.capitalize()
print(list(map(fomatStr,['jack','tom','lucy'])))

def prod(x,y):
	return x*y
print('阶乘')
print(reduce(prod,[1,2,3,4,5,6]))

import math

def is_sqr(x):
   return math.sqrt(x)%1 == 0

print (list(filter(is_sqr, range(1, 100))))


