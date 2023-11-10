#object类
#object类是所有类的父类，因此所有类都有object类的属性和方法。
#内置函数dir()可以查看指定对象所有属性
#object有一个__str__()方法，用于返回一个对于"对象的描述"，对应于内置函数str()经常用于print()方法，帮我们查看对象的信息
#经常会对__str__()进行重写

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('name:{0},age:{1}'.format(self.name,self.age))
    def __str__(self):
        return 'name:{0},age:{1}'.format(self.name,self.age)

o = object()
p = Person('Jack',20)
print(dir(o))
print(dir(p))
print(p)
    
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'My name is {0},{1}  years old'.format(self.name,self.age)

stu = Student('kaixuan',20)
print(dir(stu))
print(stu)
print(type(stu))


