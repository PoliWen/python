#自定义一个计算斐波拉契数列的模定定块
print('这是自己定义的一个模块')#在模块里面也可以写一些初始化的执行代码
if __name__ == '__main__':#这个判断使函数本身在运行的时候执行，在被其他文件引用的时候不被执行
	print('我本身在运行')
else:
	print('我是被引用过来的')
def fibo1(n):
	a,b = 0,1
	while b<n:
		print(b,end=" ")
		a,b = b,a+b
	else:
		print('')
def fibo2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
