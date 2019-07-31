#这一章节我们来学习元组Tuple的使用
tup = (1,2,3,4,5,6)
tup1 = ('a','b','c','d','e')
print(tup)
print(type(tup))
print(tup[0])
print(tup[0:3])
print(tup+tup1)#元组是不能修改的，但是可以进行拼接,使用+号可以拼接两个元组
print(len(tup))
for i in tup:
	print(i,end='')
print(('Hi')*4)
print(8 in tup)
print(max(tup))
print(min(tup))
list1 = ['111','222','3333']
tup2 = tuple(list1)#tuple函数将列表转换为元组
print(list1)
print(tup2)
print('好了啦，今天的元组学习就到这里了，下一节学习字典的数据类型')