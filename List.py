# 这一章节学习list列表的使用
list0 = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e', 'a']
print(list0[0])
print(list1[0:])
list1[0] = 111
print(list1)
del list0[0]
print(list0)
print(len(list0))
print(list0 + list1)  # 将两个列表合并
print(['Hi!']*4)
print(3 in list1)
stt = ''
for i in list0:  # 用for循环数组
    stt = stt+i
print('========================================')
print(stt)
print('========================================')
list1.append('6')  # 使用append往列表中添加新的元素
print(list1)
print(list2.count('a'))  # 计算某一个元素出现的位置
list1.reverse()  # 翻转
print(list1)  # reverse翻转
# print(list2.clear()) #清空列表
list1.pop()  # 删除最后的元素,pop(2)如果带参数的话，则是删除指定参数上的元素
print(list1)
list1.pop(2)
print(list1)
list1.insert(1, '111')  # 往指定的位置插入一个元素
print(list1)
list3 = list(range(5))  # list将元组转为列表
list1.extend(list3)  # 拓展一个数组，合并两个列表
print(list1)
print(list1.index('111'))  # index()查找某一项的位置
list1.remove('111')  # list.remove()移出列表的某一项
print(list1)
'''
多行注释
'''
print(','.join(list2))  # list转string
list4 = list(('apple', 'banana', 'cherry'))  # list()方法将一个元组转化为列表
print('*'*30)
list4.clear()
print('使用clear()方法清空列表', len(list4))
# del list4  # 使用del函数清空列表
print(type(list4))
print(repr(list4))

'''
list相关的练习题
请利用切片，取出：0-100中的
1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。

'''

L = range(1, 101)

print(L[0:10])
print(L[2::3])
print(L[4:50:5])

'''
请利用列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]

提示：range(1, 100, 2) 可以生成list [1, 3, 5, 7, 9,...]

知道基础的代码就去多都代码，多思考代码

'''
print([x*(x+1) for x in range(1, 100, 2)])


'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

'''
print([x*100+y*10+z for x in range(1, 10) for y in range(0, 10)
       for z in range(0, 10) if x*100+y*10+z == z*100+y*10+x])

'''
不学会难点，你这辈子都这样了
'''
# 如果你对一个概念不了解释因为你没找到生动的例子而不是你笨，学东西一定要想办法找到生动的例子


# 所有语言的元组都是这些东西
