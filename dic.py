#这一章节我们来学习dictionary这一数据结构
#其实你并不傻，你并不别人差，因为你总是自我怀疑不自信，导致你的能力越来越差
#什么字典，说的这么高大上，其实不就是javascript里面的json数据格式吗

#学习完Python,我能用python为我做什么

#其实学习后端是很简单的事情，不就是建表，创建数据库，然后增删改查吗，为什么你觉得数据库，难，自己学习一点点，就退缩，打退堂鼓，根本没有用心去好好学习过，就觉得自己学不会，就否定自己
import json
dic = {'name':'wxl','age':'29','target':'实现财富自由'}
print(dic)
dic['target'] = '年薪30万'
print(dic)
dic['weight'] = '62kg'#添加一个新键值对
print(dic)
del dic['weight']#del删除某一项
print(dic)
print(len(dic))
print(str(dic))
print(type(dic))
print('weight' in dic)
print(dic.items())
for i,j in dic.items():#使用此方法遍历一个dictionary字典
	print(i,':\t',j)
dic.pop('age')
print(dic)
dic.clear() #清空一个dic字典
dic = dict(name="文孝礼",age='28',target="年薪30万")
print(dic)
print('target' in dic)

x = {
	'name':'文孝礼',
	'age':'29',
	'target':'年薪30万'
}
y = json.dumps(x,indent=4) #字典转字符串
print(type(y))
print(x)

s = '{ "name":"wxl", "age":"29", "target":"年薪30万"}'
ss = json.loads(s)
print(ss['age'])
print(type(ss))

