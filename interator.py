#这一节学习迭代器
import sys
list1 = [1,2,3,4,5]
it = iter(list1)#创建一个迭代器 interator
print(next(it))
print(next(it))
for i in it:
	print(i)
while True:
	try:
	   print(next(it))
	except StopIteration:#try except 是用来解决python出错异常的
	   sys.exit()
#自己定义一个interator迭代器）
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
 
for x in myiter:
  print(x)


