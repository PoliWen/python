#这一节来学习set集合的使用，集合就是高中学数据那种集合{a,b,c,d,e,f,g}
#集合的特征，1.确定性 2.互异性 3.无序性
#中秋的夜，微凉，却始终看不到月亮
#我想她一定是害羞了，悄悄的躲到了乌云的后面
#嗯，就是这样的，我TM太机智了

a= set('hello python this is set')
thisset = set(('yes','I','can','belive','you','self'))
print(a)
thisset.add('123')
thisset.update(['aaa','bbb'])
thisset.remove('aaa')
x = thisset.pop() #随机删除某一个元素
print(thisset)
print(x)

sett = set(['aaa','bbb','ccc','ddd']) #使用set函数还可以将元组，列表转化为集合
sett.add('eee') #添加一个元素到集合
sett.update(['fff','ggg'])
print(len(sett))
sett.remove('aaa')
sett.pop() #随机删除一个
print(sett[0])
print(sett)  #集合是无序的，每次刷新都返回不同的结果
#del sett #删除这个集合
for x in sett:
	print(x)
print('aaa' in sett)

#非空集合使用set()创建，不能使用{}创建
s = set()






#python字典的使用场景

#哎，我是多么的喜欢诗句啊，中秋节，多想，多想提一壶小酒，约三五朋友，驾一叶扁舟，迷失在江南故乡的水里，小舟荡清波，过万水千山，好的程序应该像诗一样美





