'''
@Author: kingw
@Date: 2020-03-07 15:59:36
@Description: file content
'''
#python中标准输入和输出使用str,和repr
for i in range(1,11):
    print(repr(i).rjust(2),repr(i*i).rjust(3),repr(i*i*i).rjust(4))

for i in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(i,i*i,i*i*i))
