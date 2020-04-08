'''
@Author: kingw
@Date: 2020-03-13 11:52:53
@Description: file content
'''
#写一个修改文件前后缀的程序
import os
import sys
import re
#关于os的常用方法，https://blog.csdn.net/qq_29592829/article/details/83151499
#os.mkdir()创建一个文件夹,os.stat()获取文件的属性 os.path.getsize()获取文件的大小，os.
#给文件添加前缀.os.path.abspath()获取文件的绝对路径，os.path.isabs()判断路径是否是绝对路径
#os.path.exists() 判断文件是否存在
def add_suffix():
    suffix = input('请输入你想添加的前缀:')
    #这里要进行验证，只能输入英文
    data_path = os.path.abspath('../backupdata')
    listdir = os.listdir(data_path)
    for fi in listdir:
        old_name = fi
        file = os.path.join(data_path,old_name)
        newfile = data_path+'/'+suffix +'_'+ old_name
        if os.path.isfile(file):
            #要获取绝对路径才能够使用isfile来进行判断
            os.rename(file,newfile)
            print(f'{old_name}改成为{suffix}_{old_name}成功')
        else:
            print(file+'不是一个文件,是一个文件夹')

#删除文件前缀
def del_suffix():
    #这里要进行验证，只能输入英文
    data_path = os.path.abspath('../backupdata')
    listdir = os.listdir(data_path)
    for fi in listdir:
        old_name = fi
        file = os.path.join(data_path,old_name)
        #re.M|re.I 忽略大小写
        match_obj = re.match(r'(.*_)(.*)',fi,re.M|re.I)
        print('match_obj',match_obj)
        #这就代表没有匹配到
        if match_obj:
            suffix = match_obj.group(1)
            new_name = match_obj.group(2)
        else:
            print('not match')
            return
        newfile = data_path+'/'+ new_name
        if os.path.isfile(file):
            #要获取绝对路径才能够使用isfile来进行判断
            os.rename(file,newfile)
            print(f'{old_name}改成为{newfile}成功')
        else:
            print(file+'不是一个文件,是一个文件夹')
#主要执行函数
def main():
    while True:
        f = int(input('你需要添加还是删除前缀1.添加，2.删除，3.退出'))
        if f==1:
            add_suffix()
        elif f==2:
            del_suffix()
        else:
            exit()

if __name__=="__main__":
    main()
