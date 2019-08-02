#输入和输出
str1 = 'hello input'
print(str1)
print(str(str1))
f = open('os/test.txt','w')  #新建一个文件并且往文件里面写入东西，这就可以做自动化的东西啦
f.write('python is so easy and intresting!')
f.close()