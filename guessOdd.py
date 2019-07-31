#if elif可以嵌套到if里面
num = int(input('请输入一个数字'))
if num%2==0:
	if num%3==0:
		print(num,'可以同时被2和3整除')
	else:
		print(num,'可以被2整除但是不能被3整除')
else:
	if num%3==0:
		print(num,'可以被3整除，但是不能被2整除')
	else:
		print(num,'既不可以被3整除，也不可以被2整除')