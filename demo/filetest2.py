'''
@Author: kingw
@Date: 2020-03-07 16:23:11
@Description: file content
'''
fs = open('file/aaa.txt','r',encoding='utf-8')
#line = fs.readline()
#lines = fs.readlines()
#content = fs.read()
#print('line',line)
for x in fs:
    print(x,end="")
#print('lines',lines)
fs.close()

