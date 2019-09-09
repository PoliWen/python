#这一节学习python爬虫html解析工具beautifulsoup插件的使用
html_doc = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''
# beautifulsoup官方使用文档:https://beautifulsoup.readthedocs.io/zh_CN/latest/
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)
print(soup.p['class'])
print(soup.a)
# find_all查找所有的
print(soup.find_all('a'))
#find只查找匹配的第一个
print(soup.find(id='link3'))
print('='*30)
print(soup.find_all('a',class_='sister')) #返回一个列表
print('正则匹配查找')
print(soup.find(class_ = re.compile('itl'))) #正则匹配查找
print('通过属性查找')
print(soup.find_all('a',attrs={'class':'sister'})) #真是很厉害，各种匹配查找方法，其实底层逻辑就是正则表达式匹配，类似jquery
#find函数还可以传递一个返回True或者false的方法
def has_six_characters(css_class): #判断一个class是否有六个字符
    return css_class is not None and len(css_class)==6
print('返回class只有六位长度的结果')
print(soup.find_all(class_ = has_six_characters))

#从文中找到所有a标签的链接
for link in soup.find_all('a'):
    print(link.get('href'),link['id'],link.string)

# 从文档中获取所有文本内容
print(soup.get_text())

#还有 soup.find_parent();soup.find_parents();soup.find_siblings();soup.find_sibling();soup.find_next_all();soup.find_next();soup.find_all_next();soup.find_all_previous();soup.find_previous()

#soup.select()选择器，有这么多选择的方法已经够用了呢，使用的方法跟jquery的选择器方法一样，世界又是如此神奇的联系在了一起








    