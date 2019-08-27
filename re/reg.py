# python正则表达式
import re
txt = 'The rain is Spain'
print(re.match(r'(.*)( Spain$)', txt, re.I | re.M).group(1))
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
