#用python写一个裴波拉切数列 1,1,2,3,5,8,13,21.....
a,b=0,1
while b<1000:
	print(b,end=',')
	a,b = b,a+b

