print('''从今天开始好好我要好好学习python并且用python作为自己的工具，
	来爬取信息，做大数据分析，学习程序不要有负担，带着好玩的心态去学习''')
print('hello python!')
if True:
	print('True')
else:
	print('False')
print('学习编程是一件非常简单的事情，只要每天坚持学习一到半个小时，就可以轻松掌握一门语言')
word = 'word'
sentence = 'This is a sentence'
paragragh = '''this is a
paragragh'''
print('-------------------')
print(sentence*2)
print(word + ' '+ sentence)
print(r'\n\(~_~)/)')  #使用r标记，特殊字符就不会进行转义了
#字符串截取  str(头下标:尾下标)
print (word[1:3]) #截取下标1到3，但不包含下标3
x='a'
y='b'
print(x)
print(y)
print(x,end=' ')  #使用 end=' ';print输出来的信息不会进行换行
print(y,end='')
input('\n\n\n\n按下enter键退出') 
para = x + \
y+\
'xxx'   #python一行输入一句代码，可以使用+\让代码换行
print(para)
'''函数与类之间使用空格分开方便代码的阅读与维护，空格不是python的语法，空格的意义在于分隔两段
同一行显示多条语句使用;隔开'''
import sys;one = 'one';sys.stdout.write(one)

#导入python模块
import sys
print('================Python import mode===================')
print('命令参数为')
for i in sys.argv:
	print(i)
print('\n Python路径为',sys.path)

print('程序都是相通的，你应该学会那些不变的东西，然后以不变应万变，其他的语言只不过是熟悉语法而已')

#python中的变量不需要申明，但是在使用的时候必须要给其赋值，Number类型主要有int,float,bool,complex(复数)四种类型

#python 有六种数据类型分别是 Number,String,List（列表）,Tuple（元组）,Set（集合）,Dictionary（字典）

a,b,c,d,e = 1,0.3,'dd',1+4j,True
print(type(a),type(b),type(c),type(d),type(e)) #使用type()函数来判断数据的类型

a = True
print(isinstance(a,bool))#isintance(a,int)用来检测某个数据类型，返回一个bool值

print(10/3)#返回float数
print(10//3)#取整
print(10%4)#取模

list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d']
print('=======list数据类型=======')
print(list1[0:3])
print(list1*2)
print(list1+list2)#使用“+”就可以把两个list数据类型合并起来
list1[0]='111'
list1[1:3]=['222','333']
print('==========list数据类型是可以修改的===============')
print(list1)#list还有很多方法 如appen,pop










