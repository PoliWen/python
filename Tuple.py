# 这一章节我们来学习元组Tuple的使用
tup = (1, 2, 3, 4, 5, 6)
tup1 = ('a', 'b', 'c', 'd', 'e')
print(tup)
print(type(tup))
print(tup[0])
print(tup[0:3])
print(tup+tup1)  # 元组是不能修改的，但是可以进行拼接,使用+号可以拼接两个元组
print(len(tup))
for i in tup:
    print(i, end='')
print(('Hi')*4)
print(8 in tup)
print(max(tup))
print(min(tup))
list1 = ['111', '222', '3333']
tup2 = tuple(list1)  # tuple函数将列表转换为元组
print(list1)
print(tup2)
del tup2  # 删除一个元组
print('好了啦，今天的元组学习就到这里了，下一节学习字典的数据类型')

# 元组的使用场景
# 1.字符串格式化
print('我叫%s,我今年%s' % ('文孝礼', '28岁'))

# 调换两个变量的值
a = 2
b = 5
a, b = (b, a)
print(a)
print(b)

# 给变量赋值，类似于js的解构赋值，所有的编程程序都是相通的呢，一通百通，学会基础知识，就是一个字干
a, b, c, d = ('aa', 'bb', 'cc', 'dd')
print(a)

# 给函数传值


def add(*args):
    sum = 0
    print(type(args))
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))

info = 10, 20
print(type(info))
