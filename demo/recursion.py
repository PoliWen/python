# 学习几个递归函数的写法
# 计算n的阶乘
import random


def fn(n):
    if n == 1:
        return 1
    else:
        return n*fn(n-1)


print('10的阶乘是：', fn(10))

# 写一个盗梦空间程序，如果被dead或这种kicked了就醒来

print('这是一个盗梦空间程序，原创来自李笑来的《自学是一门艺术》')


def in_dream(day=0, dead=True, kicked=True):
    dead = not random.randrange(0, 10)
    kicked = not random.randrange(0, 10)  # 为什么一出手错，因为你练习的不够呀
    print('dead:', dead, 'kicked:', kicked)
    day += 1
    if dead:
        print(f'I slept {day},and was dead to wake up ...')
        return day
    if kicked:
        print(f'I slept {day},and was kicked to wake up ...')
        return day
    return in_dream(day)


print('The in_dreams function returns', in_dream())
