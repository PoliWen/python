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
print(list0+list1)
print(['Hi!']*4)
print(3 in list1)
stt = ''
for i in list0: #用for循环数组
	stt=stt+i
print('========================================')
print(stt)
print('========================================')
list1.append('6')#使用append往列表中添加新的元素
print(list1)
print(list2.count('a'))#计算某一个元素出现的位置
list1.reverse()#翻转
print(list1)#reverse翻转
#print(list2.clear())
list1.pop()#删除某位的元素
print(list1)
list1.pop(2)
print(list1)
list1.insert(1,'111')#往指定的位置插入一个元素
print(list1)
list3 = list(range(5))
list1.extend(list3)#拓展一个数组
print(list1)
print(list1.index('111'))#index()查找某一项的位置
list1.remove('111')#list.remove()移出列表的某一项
print(list1)
print(','.join(list2))#list转string

