#python正则表达式
import re
txt = 'The rain is Spain'
print(re.search('The',txt).span())
print(re.findall('ai',txt))
print(re.split('\s',txt))
print(re.sub('\s','9',txt)) #替换
