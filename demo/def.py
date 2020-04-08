'''
@Author: kingw
@Date: 2020-03-07 10:43:43
@Description: file content
'''
#关于定义一个函数
def area(w,h):
    return w*h
print('宽度为100，长度为10的长方形的面积是：',area(100,10))

#函数传递不可变对象
def changeMe(list):
    list.append([4,5,6,7])
    print("函数内部调用的值是:",list)
    return list
list=[1,2,3]
changeMe(list)
print("函数外部调用list的值是：",list)

#传递一个默认参数
def introMyself(name,age=30):
    print("我的名字是：",name)
    print("我的今年的年龄是：",age)
introMyself("文孝礼")

#不定长参数使用*，参数带一个*号，代表参数是用一个元组进行传递的
def printInfo(args,*argsTulp):
    print(args)
    print(type(argsTulp))
    for i in argsTulp:
        print(i)
printInfo(1,2,3,4,5)

#参数使用**，代表传入的就是一个字典
def printInfo2(args,**argsDic):
    print(args)
    print(type(argsDic))
    print(argsDic['a'])
printInfo2(1,a=2,b=3)

#lambda匿名函数
sum = lambda args1,args2:args1+args2
print(sum(1,2))
print(sum(2,3))

#坚持100天，每天写100行的有效代码
#坚持100天，每天写200行的有效代码
#坚持100天，每天写300行的有效代码
#你的信念，程序改变生活，你的信念，一切皆有因果，分析原因