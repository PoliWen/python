'''
@Author: kingw
@Date: 2020-03-09 09:56:03
@Description: file content
'''
#python中定义类
class people:
    name=''
    age=0
    __weight='8kg'
    __height='170cm'
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age=age
        self.__weight = weight
        self.__height = height
    def print_info(self):
        print(f'我的名字叫做{self.name},我今年{self.age}岁,我的体重是：{self.__weight},我的身高是：{self.__height}')
class speck:
    topic = '我演讲的主题是如何成为一名高手'
    def __init__(self,topic):
        self.topic = topic
    def speaking(self):
        print(f'我演讲的主题是{self.topic}')
class woman(people,speck):
    sex = 'woman'
    def __init__(self,name,age,weight,height,sex,t):
        people.__init__(self,name,age,weight,height)
        speck.__init__(self,t)
        self.sex = sex
    def print_info(self):
        print(f'我的名字叫做，我的性别是{self.sex}')


p = people('文孝礼',30,'61kg','176cm')
p.print_info()
w = woman('小祝',28,'50kg','168cm','woman','好好学习python')
w.print_info()
w.speaking()
#在子类中调用父类的方法
super(woman,w).print_info()