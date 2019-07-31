#利用if条件判断做一个猜数字的游戏
number = 7
guess = -1
while guess != number:
	guess = int(input('请输入你猜的数字'))
	if guess == number:
		print('恭喜你猜对了')
	elif guess<number:
		print('你猜小了...')
	elif guess>number:
		print('你猜大了...')

