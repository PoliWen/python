'''
@Author: kingw
@Date: 2020-03-06 11:14:12
@Description: file content
'''
#python中与字符串相关的操作
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
a= "hello"
b="python"
print("a+b,字符创链接用+",a+b)
print("a*3",a*3)
print("a[1:]",a[1:])
print("a[1:4]",a[1:4])
if('h' in a):
    print(True)
else:
    print(False)
if('p' not in b):
    print(True)
else:
    print(False)
#字符串格式化
print("我叫%s今年%d岁"%('文宇',30))  #这个和java差不多一样

#使用format方法更方便灵活
print("{0} {1} {0}".format('hello','python'))
#format函数还可以使用字典，也可以调用数组
print("网站名：{name},网站地址：{url}".format(name="百度",url="www.baidu.com"))
my_list = ["菜鸟教程","http://www.runood.com"]
print("网站名:{0[0]},网站地址:{0[1]}".format(my_list))
#'''使得程序员从用+号拼接字符串里面解脱出来了，类似于js里面的``符号
print('''
(\t)[\n]
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
prid INTEGER)
''')
#f'{x}'类似于js里面的${}
x=99
print(f"x+1={x+1}")
str = "google#hello#word#python is so easy!"
print(str.split('#',2)) 
print(str.split('#'))
seq = ['2020','03','06']
print('-'.join(seq))
#写程序不应该只是写来玩一玩的，应该用程序去解决生活中的一些问题
str = "     "
#isspace判断一个字符串里面是不是都是空格
print(str.isspace())
str="i love you"
#capitalize首字母大写
print(str.capitalize())
print(str.capitalize().center(100,'*'))
#count统计一个一个字符串里面的某一个单子字符出现的次数
print(str.count('o',3,))
#encode('utf-8','stric') 编码
#decode('utf-8','stric) 解码
str = '学习编程是一件非常\t简单的容易的事情'
#str.expandtabs用来将tab换行字符转化为空格，一个\t转化为8个空格
print("############",str.expandtabs())
str_utf8 = str.encode('UTF-8') 
str_gbk = str.encode('GBK')
print(str_utf8)
print(str_gbk)
str_utf8_decode = str_utf8.decode('UTF-8','strict')
str_gbk_decode = str_gbk.decode('GBK','strict')
print(str_utf8_decode)
print(str_gbk_decode)
#endswith用来判断某一个字符串是否以某一个后缀结尾，返回一个boolen值
print(str.endswith('情'))
print(str.find('是'))
print(str.index('是'))
str="123456"
#isdigit判断是否是一个数字,返回一个boolean值
print(str.isdigit())
#islower判断是否都是小写字母
print('Aaaaa'.islower())
#len()输出字符串的长度
print(len(str)) #输出结果6
#lower将所有的字母转化为小写字母
print("AAAAAA".lower())
#strip去除前后的空格，lstrip去除左边的空格，rstrip去除右边的空格
print("    ggg   ".strip())
#startwith()判断字符串是否以某一个前缀开始
print('aaa'.zfill(50))

