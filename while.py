#这一章节学习python的while循环
n = 100
sum = 0
counter = 1
while counter <= n:
	sum += counter
	counter += 1
else:
	print('counter已经大于 %d 了'%(n))#else在while的条件结束的时候执行
print('1到 %d之和 %d ' % (n,sum))#格式化字符串,你需要优化这个算法


