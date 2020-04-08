'''
@Author: kingw
@Date: 2019-09-09 18:42:05
@Description: file content
'''
# 输出一个文件夹下的所有文件夹列表以及输出文件夹
import os
import re
# os.mkdir('demo')
# os.mkdir('wxl')
# os.mkdir('hahaha')

dirpath = './os/'
filelist = os.listdir(dirpath)
def add_mark():
    mark = input('请输入你要添加的前缀')
    for oldname in filelist:
        curdir = os.path.join('./os/',oldname)
        if os.path.isfile(curdir):  # 是文件才替换，文件夹不进行替换
            if not os.path.exists(oldname):
                os.rename(dirpath+oldname, dirpath+mark+oldname)
                print('您已经成功为'+oldname+'添加'+mark+'前缀')


def remove_mark():
    mark = input('请输入你要删除的前缀')
    for oldname in filelist:
        curdir = os.path.join('./os/',oldname)
        print(os.path.isfile(curdir))
        if os.path.isfile(curdir):         # isfile必须是绝对路径
            try:
                result = re.match(r'(%s)(.*)'%(mark), oldname).group(2)
                if result:
                    os.rename(dirpath+oldname, dirpath+result)
                    print('您已经成功为'+oldname+'删除'+mark+'前缀')
            except Exception as e:
                print(e)


def main():
    option = int(input('输入你想执行的操作:\n1.添加前缀。\n2.删除前缀。\n3.删除前缀\n'))
    if option == 1:
        add_mark()
    elif option == 2:
        remove_mark()
    else:
        exit()


if __name__ == '__main__':
    main()  # 如果是执行当前文件那么就是执行main函数

# 写代码其实很简单，very easy，先把框架搭起来，在一步步去填充，去写代码
