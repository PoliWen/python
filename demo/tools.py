'''
@Author: kingw
@Date: 2020-03-07 15:12:24
@Description: file content
'''
#定义一个斐波拉契数列
print('xxxooo')
def fibo(n):
    a,b=0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()
def fibo2(n):
    a,b=0,1
    result=[]
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
if __name__=='__main__':
    print('只有执行本身的时候才运行，而在引入其他文件中的收不执行')
    print('xxxxxx')
    print(__name__)

