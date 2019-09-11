# python字符串的学习
word = 'hello python,python is so easy\a'
print('nmb', 'nigesx')  # 多个参数用逗号隔开，输出的时候以空格分开
print(word)
print(word[0:6])
print(word[-1:])
print(word[0:])
print(word[0:6:2])
print(word[3])  # 访问string中的字符串
print(word + '+的符号是用来拼接字符串的')
print(word*3)  # *是用来重复输出字符串的，这里输出3次
if('h' in word):  # 使用in来判断字符串是否在一个字符串中
    print('h is in word')z
else:
    print('h is not in word')
if('g' not in word):  # 使用not in来判断某一个字符不属于某一个字符串
    print('g is not in word')
else:
    print('g is in word')
print(r'\n\(~_~)/')  # r对特殊的字符串不进行转义
print('''三引号的使用，这是一个非常棒的东西，
还可以输出转义字符串例如tab(\t),\n换行符\n
三行运算符，来写html片段和mysql语句是非常好用的
,''')

print('h'.capitalize())  # capitalize()将字符串的首字母大写
print(len(word))  # len(str)返回字符串的长度
print('+'.join(word))  # 将字符串用某一个特殊的字符串连接起来
str = 'That is a string example...wow!'
print(str.replace('is', 'was'))  # replace用来代替替换字符串的字符
print(str.upper())  # upper将字符串全都转化为大写
print(str.center(100, '='))  # center返回一个固定的宽度的居中的字符串，剩余的用fillchar填充
strlstrip = '     Lstrip是可以用来截取左边的空格，或者去除左边的指定字符    '
print(strlstrip.lstrip().rstrip())
cstr = strlstrip.center(200, '+')  # rstrip跟左边的一样的
print(cstr.lstrip('+').rstrip('+').lstrip().rstrip())
print(cstr.strip('+').strip())  # 去除前后空格，和前后指定字符串
print(str.split(' '))  # split将字符串切割成一个list数组,第二个参数num指的是将字符串切割成num+1项
print(str.split(' ', 1))
print(str.lower())  # 将所有字符串转换为小写
print(str.count('i', 0, len(str)))  # count(sub,start=0,end=len(string))
print(str.find('is'))  # find是用来查找某一个字符首次出现的位置
print(str.find('is', 10))  # 后面两个参数指定查找的范围
print(str.index('is'))  # index跟find方法一样
print('到此字符串的学习就告一段落了，接下来学习列表的数据结构')

print(ord('a'))
print(chr(122))
