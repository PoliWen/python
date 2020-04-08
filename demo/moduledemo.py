'''
@Author: kingw
@Date: 2020-03-07 15:14:42
@Description: file content
'''
from tools import fibo,fibo2
import sys
#dir方法用来查看导入的一个类里面的所有方法
print(dir(sys))
if __name__=="__main__":
    fibo(1000)
    print(fibo2(1000))
    #这真是的very good


