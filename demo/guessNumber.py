'''
@Author: kingw
@Date: 2020-03-07 09:15:18
@Description: file content
'''
#写一个猜数游戏
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
number = 10
guess = 1
while guess!=number:
    guess = int(input('请输入你猜的数字'))
    if guess==number:
        print('恭喜您猜对了')
    elif guess>number:
        print("猜大了...")
    else:
        print("猜小了...")