# python正则表达式
import re
txt = 'The rain is Spain'
# match从第一个开始匹配
daoyan = '''
                            导演: 吕克·贝松 Luc Besson   主演: 让·雷诺 Jean Reno / 娜塔莉·波特曼 ...'''
print(re.search(r'^.*导演:(.*\s{3}).*', daoyan, re.I | re.M).group(1)) 
print(re.match(r'(.*)( Spain$)', txt, re.I | re.M).group())
print(re.findall('ai', txt))
print(re.split('\s', txt))
print(re.sub('\s', '9', txt))  # 替换
with open('ret.txt', 'r') as f:
    str1 = f.read()
print(str1)
pattn = r'[A-z]\w+'
pattn2 = r'go+gle'  # +匹配>=1次
pattn3 = r'go{2,5}gle'  # 匹配n次或者m次
pattn4 = r'520*'  # 匹配任意次
pattn5 = r'colou?re'  # ?匹配0次或者1次
print(re.findall(pattn, str1))  #
print(re.findall(pattn2, str1))
print(re.findall(pattn3, str1))
print(re.findall(pattn4, str1))
print(re.findall(pattn5, str1))

str3 = 'The white dog wears a black hat.'
pttn = r'The (white|black) dog wears a (white|black) hat.'
# 把字符串里面的都包含大写字母的字符串都给找出来替换并且换回去
repl = r'the \2 dog wears a \1 hat.' #分组匹配
print(re.sub(pttn,repl,str3))
repl2 = r'the \1 dog wears a \2 hat.'
print(re.sub(pttn,repl2,str3))  #分组匹配