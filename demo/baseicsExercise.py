'''
@Author: your name
@Date: 2020-03-05 11:42:40
@LastEditors: Please set LastEditors
@LastEditTime: 2020-03-06 10:17:21
@Description: file content
'''
###重新重头来复习python的基础知识
a,b,c,d,e = 1,3.14,True,4+3j,'python is so easy'
print(type(a),type(b),type(c),type(d),type(e))
print(isinstance(a,int))
##python中的常见运算
print(2**5)#平方计算
print(5%2) #取模运算
print(5/2) #除法得到一个小数
print(5//2)#除法得到一个整数
list = [123,456,789,'aaa','bbb']
list[0] = 000
print(list)
list[2:4] = [111,222]
print(list)
if (000 in list):
    print (True)
else:
    print(False)

if(a and b):
    print(True)
else:
    print(False)
