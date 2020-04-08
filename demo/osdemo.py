'''
@Author: kingw
@Date: 2020-03-09 11:48:09
@Description: file content
'''
#os库
import os
import glob
#通过一个通配符来查找文件
print(glob.glob('*.py'))
print(dir(os))
print(os.getcwd())
print('当前目录下包含的文件',os.listdir(os.getcwd()))


