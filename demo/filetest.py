'''
@Author: kingw
@Date: 2020-03-07 16:16:20
@Description: file content
'''
#python中读取文件的方法
f = open('file/aaa.txt','w',encoding='utf-8')
num=f.write('python是一个非常好的语言，\n是的的确\n,非常好')
print('往文件里面写入内容成功,写入了：',num,'个字符')
f.close()
