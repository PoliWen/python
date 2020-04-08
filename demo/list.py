'''
@Author: kingw
@Date: 2020-03-06 16:17:14
@Description: file content
'''
#列表,list
list1 = [1,2,3,4,5,6,2]
list2 = [7,8,9,10,11]
print(list1)
#del用来删除list的某一个元素
del list1[2]
print(list1)
for x in list1:
    print(x) #加参数end=""返回的字符串不换行
print(list1+list2) #用+来连接两个list
#max返回list里面最大的值
print(max(list1))
#min返回list里面最小的值
print(min(list1))
#len()返回数组的大小
print(len(list1))
print(list(range(5)))   #创建一个0-5的列表
#append往list的后面追加元素
list1.append('8')
print(list1)
#count()统计某一个元素在一个list里面出现的次数
print(list1.count(2))
#extend往一个list后面添加拓展一个list
list2.extend(list(range(10)))
print(list2)
#index查找某一个元素在数组中的当前序列号
print(list2.index(1))
#insert往list指定的位置插入元素
list2.insert(1,'ggggg')
print(list2)
#pop()删除list尾部的一个元素
list2.pop()
list2.remove(11)
print(list2)
#reverse翻转list
list2.reverse()
print(list2)
#sort排序,字符串不能和数字在一起进行比较
sortdemo = [5,4,3,2,7,9]
sortdemo.sort()
print(sortdemo)
