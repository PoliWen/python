#这一节来学习set集合的使用，集合就是高中学数据那种集合{a,b,c,d,e,f,g}
a= set('hello python this is set')
thisset = set(('yes','I','can','belive','you','self'))
print(a)
thisset.add('123')
thisset.update(['aaa','bbb'])
thisset.remove('aaa')
x = thisset.pop()#随机删除某一个元素
print(thisset)
print(x)

