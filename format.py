#格式化输出
for x in range(1,11):
	print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))
print('12'.zfill(10))
print('10'.rjust(10))
print('10'.center(40,'*'))
print('{0}{1}{other}'.format('文小李','29',other='男'))

table = {'name':'文小李','age':'29'}
for k,v in table.items():
	print('{0:10}==>{1:10}'.format(k,v))

	