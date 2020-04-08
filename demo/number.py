'''
@Author: kingw
@Date: 2020-03-06 10:21:43
@Description: python中与数字的相关的方法
'''
import math
import random
#########解决中文输出乱码的问题###########
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
####################
print(round(3.64))  #四舍五入
print(math.ceil(3.14)) #向上取整
print(math.floor(3.14)) #向下取整
print(math.sqrt(16)) #开平方根
print(math.pow(3,4)) #平方 结果等于 3**4
print('对数运算',math.log(16,2)) #对数运算
print(3/4) #除以含小数
print(3%4) #取模运算
print(3//4) #除以取整运算
#random.choice()随机从一个数组里面取出一个数字
random.choice(range(10))
####随机数
print(range(10))
#random.random()返回一个随机0到1之间的随机数
print("random:",random.random())

##randtange 返回一个指定步长的随机数
print(random.randrange(1,100,2))
#####每天用python做一个小demo



