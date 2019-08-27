# 这一章节学习python的while循环
n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1
else:
    print('counter已经大于 %d 了' % (n))  # else在while的条件结束的时候执行
print('1到 %d之和 %d ' % (n, sum))  # 格式化字符串,你需要优化这个算法

i = 0
while i < 6:
    print(i)
    if i == 3:
        break  # break跳出当前循环，所有的程序都是相通的啊，大哥，基础知识过一遍就好了，剩下的一个字就是干
    i += 1
print('-'*30)
j = 0
while j < 6:
    print(j)
    j += 1
    if j == 3:
        continue
