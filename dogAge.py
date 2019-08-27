# 写一个demo计算狗狗相对于人类的年龄
dogAge = int(input('您的狗狗今年多少岁: '))
print("")
if dogAge < 0:
    print('你在开玩笑吧！')
elif dogAge == 1:
    print('相当于14岁的人类')
elif dogAge == 2:
    print('相当于22岁的人类')
elif dogAge > 2 and dogAge < 20:
    human = 22+(dogAge-2)*5
    print('相当于人类', human, '岁')
elif dogAge > 20:
    print('您在开玩笑吧，狗狗最大年龄一般是7到8岁呢')
input('输入enter键结束')
# 继续将其拓展，开发一个时间判断的函数，计算今天是什么时间，在结合定时器，做一个时钟，在学习完函数那一章节，完成这个任务
print('太棒了我会写一个逻辑判断了')
