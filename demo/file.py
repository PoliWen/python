# 常见的文件操作
'''
r:只读模式
w:读写模式(文件不存在则创建文件，重建)
a:追加模式（文件不存在则创建文件，在已有文件追加）
rb:二进制读取
wb:二进制写入
ab:二进制追加
'''
import os
f = open('./file/demo.txt', 'wb')  # 以二进制的方式读写文件
f.write('中文中文life is so short,so you should learn python!\n,python is so easy\n'.encode(
    encoding='utf-8'))
f.close()
print(f.name)
# 删除一个文件使用os.remove()
if os.path.exists(f.name):
    os.remove(f.name)
    print(f'{f.name} is delete.')
else:
    print(f'{f.name} is not exist.')
a_lists = ['first line\n', 'second line\n', 'thord line\n']
f2 = open('./file/demo2.txt', 'a')  # 以二进制的方式读写文件
f2.writelines(a_lists)  # 直接写入一个列表
print(f2.name)
f2.close()

f3 = open('./file/demo2.txt', 'r')
# 读取所有的行
s = f3.read()  # 读取所有的内容
print(type(s))
print(len(s))
print(s)
content = f3.readlines()  # 全面了解字符的操作
print('*'*30)
for n in content:
    print(n)

f4 = open('./file/demoins3.txt', 'w')
lists = ['first line\n', 'second line\n', 'thord line\n']
f4.writelines(lists)
f4.close()
with open('./file/demo3.txt', 'r') as f:
    print('f.seek(offset,)')
    print(f.readline())
    f.seek(id, 1)
    print(f.readline())
# 需要继续拓展训练，如何用python如何。csv文件，处理excel文件，world文件，操作文件夹，移动文件夹等等行为，越全面掌握越好
