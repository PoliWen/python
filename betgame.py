# -*- coding: utf-8 -*-
# 写一个投骰子打赌的游戏
'''
游戏规则，玩家和庄家进行完投筛子游戏
玩家和庄家各10个银币
游戏开始庄家投筛子，玩家猜大小
如果点数==7 和
如果点数<7 玩家猜小，玩家赢；玩家猜大，玩家输
如果点数>7 玩家猜大，玩家赢；玩家猜小，玩家输
当有一方的银币为零的时候，游戏结束
编程有什么难的，不过流程控制

编程就是死的，有什么问题，你就去解决什么问题，一定有办法解决的，如果没解决掉，你需要给你的大脑洗脑了，如果你觉得你很笨，用百度总是找不到你需要的东西，不是因为你真的笨而是英文百度太垃圾了

'''
from random import randrange
coin_user, coin_bot = 10, 10
rounds_of_game = 0


def bet(dice, wager):
    if dice == 7:
        return 0
    elif dice < 7:
        if wager == 's':
            print(f'the dice is {dice} you win')
            return 1
        else:
            print(f'the dice is {dice} you lost')
            return -1
    elif dice > 7:
        if wager == 'b':
            print(f'the dice is {dice} you win')
            return 1
        else:
            print(f'the dice is {dice} you lost')
            return -1


while True:
    print(f'your coin{coin_user}, bot coin{coin_bot}')
    wager = input('your bet ?')
    dice = randrange(2, 12)
    if wager == 'q':
        break
    elif wager in 'bs':
        result = bet(dice, wager)
        coin_user += result
        coin_bot -= result
        rounds_of_game += 1
    if coin_user == 0:
        print(f'Woops, you lost')
        break
    if coin_bot == 0:
        print(f'Woops,you winner')


print(f'you\'ve played {rounds_of_game}rounds')
print(f'you have coin{coin_user} now')


