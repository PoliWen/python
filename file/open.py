#这一节学习文件大打开和编辑
import sys
f = open('../os/test.txt','w',encoding='utf-8');
num = f.write('python是一门很棒，很容易学习的语言，\n 人生苦短，快学pyhon呀')
print(num)#写入字符，并且记录下写入的字符
f.close();