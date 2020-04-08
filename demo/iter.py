'''
@Author: kingw
@Date: 2020-03-07 10:39:01
@Description: file content
'''
#迭代器
import sys
list1 = [1,2,3,4]
for i in list1:
    print(i)
iter1 = iter(list1)
while True:
    try:
        print('通过迭代器访问一个list的所有对象：',next(iter1))
    except StopIteration:
        sys.exit()