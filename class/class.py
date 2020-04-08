'''
@Author: kingw
@Date: 2019-08-05 10:30:08
@Description: file content
'''
 #python定义一个类
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.__weight = weight#__为私有属性，不能被继承在子类中访问
        self.__height = height
    def speak(self):
        print("%s 说: 我 %d 岁。我的体重是%d,我的身高是：%d" %(self.name,self.age,self.__weight,self.__height))
# 实例化类
p = people('文孝礼',10,30,170)
p.speak()

#继承一个类
class student(people):
    grade = ''
    def __init__(self,name,age,weight,height,grade):
        people.__init__(self,name,age,weight,height)#调用私有属性__weight会报错，因为私有属性不能被继承
        self.grade = grade
    def speak(self): #方法的重载，那么如何调用父级的方法呢？
        super(student, self).speak()
        print("%s 说: 我 %d 岁。我今年读%s" %(self.name,self.age,self.grade))

s = student('小明',10,30,40,'三年级')
s.speak()
super(student,s).speak() #子类直接调用父类的方法

