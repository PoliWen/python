'''
@Author: kingw
@Date: 2020-03-09 17:22:51
@Description: file content
'''
#python中正则表达式的使用
import re
print(re.search('www','www.baidu.com').span()) #span方法返回匹配的字符串的位置
print(re.search('com','www.baidu.com').span())
 
line="Cats are smarter than dogs"
reObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if reObj:
    print(reObj.group())
    print(reObj.group(1))
    print(reObj.group(2))
else:
    print('none of match')
#sub方法是用来对匹配的字符串进行替换的
phone = '15012659562 #这是一个电话号码'
print(re.sub(r'#.*$','',phone))
print(re.sub(r'\D','',phone))

