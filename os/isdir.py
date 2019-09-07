# 输出一个文件夹下的所有文件夹列表以及输出文件夹
import os
# os.mkdir('demo')
# os.mkdir('wxl')
# os.mkdir('hahaha')

fileData = os.listdir('.')
print(fileData)
f1 = []
f2 = []
for x in fileData:
    if os.path.isdir(x):
        f1.append(x)
    elif os.path.isfile(x):  #哎，一个这么简单的bug找这么久，基本的语法错误都犯了
        f2.append(x)
        os.rename(x,'xxx_'+ x)
        print(x+'成功更名为:xxx_'+x)

print(f1)  #拆分出来文件夹
print(f2)  #拆分出来文件名