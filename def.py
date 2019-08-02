#def 函数定义
'''
def 函数名(函数参数):
	函数体
'''
import sys
print(dir(sys))
def area(w,h):
    print('width=',w,'height=',h,'aera=',w*h)
def welcome(name):
	print('welcome',name)

welcome('python')
area(40,50)

'''
对，学习编程就是这么简单呀
'''
def printInfo(name,age=18):
	print('name=',name,'age=',age)
printInfo(age=28,name="文孝礼")

printInfo(name="wxl")

def myfn(a,*rest):#用*varTuple来表示剩下的参数
	print(a)
	print(rest)
	for i in rest:
		print(i)
myfn('a','b','c','d')

def sum(*args):#定义一个求和的参数
	sum = 0
	for i in args:
		sum+=i
	return sum
print(sum(1,2,3,4,5))

def myfn2(a,**rest):#两个**代表传入的是一个字典数据类型
	print(a)
	for i,j in rest.items():#这个方法是遍历dictionary的字典数据结构的
		print(i,j)
myfn2('a',name="文孝礼",age="29")

#函数作用域(
num = 10
def total(num):
	#global num #想要在函数内部改变全局的num就需要使用global关键字
	num = num + 30
	print(num)
print(num)
total(num)
