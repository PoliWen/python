# 这一章节学习os的各种用法
import os
import shutil  # 这个模块主要是用来进行拷贝和移动文件的
print(dir(os))
print(os.getcwd())  # os.getcwd()返回当前工作的目录
print(os.listdir('../backupdata'))  # 返回指定目录下的所有文件名
# os.mkdir('demo')  # 创建目录
# os.remove('test.txt')  # 删除一个文件

# 这些东西用nodejs也可以搞定
print(os.path.abspath('foo.html'))  # 返回文件的相对路径
print(os.path.getsize('foo.html'))  # 返回文件的大小字节数
print(os.name)
# os.path.isdir()
# os.path.isfile()

print('*'*30)
olddir = os.getcwd()
print(olddir)
# os.mkdir('/temp')
os.chdir('/temp')
print('修改只有的目录：' + os.getcwd())
print('*'*30)
