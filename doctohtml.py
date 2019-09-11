#利用插件生成html
#读取docx文件并且按指定的格式输出html文件,可以继续拓展这个代码，带文件的怎么读取学习
#将这个方法用面向对象的方式进行改写
#author wxl
import docx  #https://python-docx.readthedocs.io/en/latest/index.html
import os
import re
from docx2html  import convert    #将world转化为html
import HTMLParser
def readdoc(sfp,dfp):
    print(sfp)
    print(dfp)
    docn = convert(sfp)
    html_parser = HTMLParser.HTMLParser()
    htmltemp = html_parser.enescape(docn)
    print('读取docx文件成功')
    with open(dfp,'w',encoding='utf-8') as f:
        f.write(htmltemp)
        print('写入docx文件成功')
    pass #对读取的world文件输出成html文件还要进行优化，按照客户的需求
#思考 这个函数是否还有优化的空间呢？读取文件夹的方式是否可以优化呢
def changetohtml(sdir,edir):
    spath = os.getcwd() + sdir #docx文件的路径
    epath = os.getcwd() + edir #docx文件的路径
    sdirArr = [spath + x for x in os.listdir(spath)]
    edirArr = [epath + x for x in os.listdir(spath)]
    def changenSuffix(str): #改变后缀函数
        return re.sub('.docx','.html',str) #将文件的后缀进行替换
    edirArr = list(map(changenSuffix,edirArr))
    print(sdirArr)
    print(edirArr)
    i = 0
    for sfp in sdirArr: #pythin循环的这个i序列号有什么好的办法处理吗？
        efp = edirArr[i]
        i += 1
        print(sfp,efp)
        readdoc(sfp,efp)
    pass
def main():
    sdir = '/docdir/'
    edir = '/htmldir/'
    changetohtml(sdir,edir)
if __name__ == '__main__':
    main()