'''
@Author: kingw
@Date: 2019-08-23 12:05:26
@Description: file content
'''
import os
import re
import sys

# 添加前缀

# 学习python,每天写200行新鲜的代码量，坚持练习下去，写下去，写100天,你就可以用python做很多的事情了
def add_mark():
    pre = input("请输入需要添加的前缀:")
    mark = str(pre)
    old_names = os.listdir('./backupdata')
    print(old_names)
    print(sys.argv[0])  # 代表输入的控制面板输入的第一个参数
    # print(sys.argv[1])
    for old_name in old_names:
        print('g'*30)
        print(old_name)
        if old_name != sys.argv[0]:
            os.rename('./backupdata/' + old_name,
                      './backupdata/' + mark+old_name)
# 删除前缀
def remove_mark():
    old_names = os.listdir('./backupdata')
    for old_name in old_names:
        print(old_name)
        try:
            #result = re.match(r"(^\[.*\]chb_)(.*)", old_name)
            result = re.match(r"(^chbchb_)(.*)", old_name).group(2)
            print('*'*30)
            print(result)
            print('*'*30)
            rm = old_name
            if result:
                os.rename('./backupdata/' + old_name, './backupdata/' + result)
            print("已为%s移除前缀" % rm)
        except Exception as e:
            print(e)
            # pass

# 主入口函数


def main():
    while True:
        option = int(input("请选择功能数值:\n1.添加前缀\n2.删除前缀\n3.退出程序\n"))
        if option == 1:
            add_mark()
        elif option == 2:
            remove_mark()
        else:
            exit()


if __name__ == "__main__":
    main()
