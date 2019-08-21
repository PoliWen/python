#这一章节学习list列表的使用
list0 = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e','a']
print(list0[0])
print(list1[0:])
list1[0] = 111
print(list1)
del list0[0]
print(list0)
print(len(list0))
print(list0 + list1) #将两个列表合并
print(['Hi!']*4)
print(3 in list1)
stt = ''
for i in list0: #用for循环数组
	stt=stt+i
print('========================================')
print(stt)
print('========================================')
list1.append('6') #使用append往列表中添加新的元素
print(list1)
print(list2.count('a')) #计算某一个元素出现的位置
list1.reverse() #翻转
print(list1) #reverse翻转
#print(list2.clear()) #清空列表
list1.pop() #删除最后的元素
print(list1)
list1.pop(2)
print(list1)
list1.insert(1,'111') #往指定的位置插入一个元素
print(list1)
list3 = list(range(5)) #list将元组转为列表
list1.extend(list3) #拓展一个数组，合并两个列表
print(list1)
print(list1.index('111')) #index()查找某一项的位置
list1.remove('111') #list.remove()移出列表的某一项
print(list1)
print(','.join(list2))  #list转string
list4 = list(('apple','banana','cherry')) #list()方法将一个元组转化为列表
print('*'*30)
print(type(list4))
print(repr(list4))



#所有语言的元组都是这些东西



