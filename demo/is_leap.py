# 判断一个年份是不是闰年
'''
根据闰年的定义：
年份应该是 4 的倍数；
年份能被 100 整除但不能被 400 整除的，不是闰年。
所以，相当于要在能被 4 整除的年份中，排除那些能被 100 整除却不能被 400 整除的年份。

先假定都不是闰年；
再看看是否能被 4 整除；
再剔除那些能被 100 整除但不能被 400 整除的年份……

'''


def is_leap(year):
    r = False
    if year % 4 == 0:
        r = True
        if year % 100 == 0:
            if year % 400 != 0:
                r = False
    return r

# dateTime里面的_is_leap()函数的更简洁的写法


def _is_leap(year):  # 再次验证一遍读不懂的时候就多都几遍,一句都不懂时，就拆解分解
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print(_is_leap(200))

# 程序的思维方法
print(is_leap(8))    # true
print(is_leap(200))  # false
print(is_leap(220))  # true
print(is_leap(400))  # true

year = range(1990, 2050)
leap_year = list(filter(is_leap, year))
print(leap_year)
