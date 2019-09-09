#这一节学习读取文件
f = open('../os/test.txt','r',encoding='utf-8')
#str1 = f.read()
#str1 = f.readline() #输出一行
str1 = f.readlines() #输出所有行
print(str1)
print(f.tell())
f.close()