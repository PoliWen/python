#这一章节我们来学习dictionary这一数据结构
#其实你并不傻，你并不别人差，因为你总是自我怀疑不自信，导致你的能力越来越差
#什么字典，说的这么高大上，其实不就是javascript里面的json数据格式吗

#学习完Python,我能用python为我做什么

#其实学习后端是很简单的事情，不就是建表，创建数据库，然后增删改查吗，为什么你觉得数据库，难，自己学习一点点，就退缩，打退堂鼓，根本没有用心去好好学习过，就觉得自己学不会，就否定自己
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
for i,j in dic.items():
	print(i,':\t',j)
print('字典的数据结构先学到这里，还有些方法不理解，下次要继续深入的学习')
