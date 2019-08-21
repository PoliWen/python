#这一章节学习if条件判断语句和while循环语句
a=1
while a < 7:
	if(a % 2 == 0):
		print(a,'is even')
	else:
		print(a,'is odd')
	a+=1
else:
	print(a,'大于7')

#python里面的三目运算

b = 6
c = 4
print('b') if b>c else print('c')
