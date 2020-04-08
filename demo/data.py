'''
@Author: kingw
@Date: 2020-03-07 11:20:47
@Description: file content
'''
#python中的数据结构
#list的增删改查，append();del;remove();insert();index();sort();count();extend();pop();reverse()

#tupl()的增删改查，不能修改，使用序列号进行访问,使用del方法，会报错，因为不能对tupl进行修改删除,可进行切片
print('###############tuple元组数据类型##################')
tupl = (1,2,3,4,5)
tupl2 = tuple(['aaa','bbb','ccc','ddd'])
print(tupl[1])
for x in tupl:
    print(x)
print(max(tupl))
print(min(tupl))
print(len(tupl))
print(2 in tupl)
print(3 not in tupl)
print(tupl*2)
print(tupl+tupl)
#del tupl[0]

#set集合的操作，不能增删,集合的特点，无序，不能重复，
print('set集合数据类型'.center(50,'#'))
a = set('fsadsfadsvbfdsrtgafdsf')
b = set('fsjkfhsfjhskfhbbdafas')
print(a)
print(b)
print('a' in a)
print(a-b)#返回一个集合的差集
print(a|b)#返回集合a和b中的并集
print(a&b)#返回a和b的交集
print(a^b)#返回a和b的
a.add('ggg')#使用add的方法往集合里面添加元素
print(a)
a.remove('a')#使用remove方法删除字典中的元素.如果在字典中不存在就会报错,而使用 discard不会报错
a.update(['a','bbb','ccc','ddd'])#使用update更新字典，参数可以是元组，列表，字典等
print(a)
a.discard('bbb') #discard也可以删除字典里面的某一个元素，如果不存在不会报错,discard的英文的意思是丢弃的意思
print(a)
b = a.pop()#随机的删除字典里面的某一个元素
print(a,b)
print(len(a)) #使用len函数计算字典里面的个数
print('x' in a)
a.clear() #使用clear()的方法清除字典
print(a)

print('dictinary字典数据结构'.center(50,'#')) #字典里面的元素
dic = {'name':'文孝礼','age':'30','weight':'61kg','height':'173cm'}
print(dic)
#修改
dic['age']=29
print(dic)
#删除
del dic['age']
print(dic)
print(len(dic))
#dic.clear()
print('name' in dic)
#这是一个浅的拷贝
import copy
dic2 = dic
dic3 = dic.copy() #这是一个浅拷贝，使用深度拷贝，需要引入copy的类
dic['weight'] = '62kg'
print(dic2)
print(dic2,dic3)
print('name' in dic)
print('dic.keys',dic.keys())
print("dic.values",dic.values())
items = dic.items() #返回字典的迭代对象
for k,v in items:
    print(f"{k}:{v}")
dic_update = {'wife':'小祝'}
dic.update(dic_update)
print('updatedic:',dic)
pop_item = dic.pop('name')
print(pop_item,dic)
pop_obj = dic.popitem()
print(pop_obj,dic)

c = [1,2,['a','b','c']]
c1 = c.copy()
c2 = copy.deepcopy(c)
c[2].append('d')
print(c,c1)
print(c2)

#为什么python里面类的方法都不是采用驼峰的方式进行命名的呢？

ajax({
      success:function(res){
          res.code
      }
})