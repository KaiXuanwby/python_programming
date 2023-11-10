#特殊属性和方法：由两个下划线开始两个下划线结束，就称为特殊的属性或者方法
#特殊属性：
#__dict__:获得类对象或实例对象所绑定的所有属性和方法的字典

#print(dir(object))


class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
#创建C类的对象
x = C('Jack',20)     #x是C类型的一个实例对象
print(x.__dict__)    #打印结果为实例对象的属性字典，得到一个字典，对象的属性为键，对象的属性值为字典当中的一个值
print(C.__dict__)    #如果为类对象，则可以看到其属性和方法组成的字典
print(x.__class__)   #输出对象所属的类
print(C.__bases__)   #输出的是父类类型组成的元组
print(C.__base__)    #输出的是和C离的最近的父类（第一）
print(C.__mro__)     #输出类的层次结构
print(A.__subclasses__())   #子类的列表



#特殊方法：
#__len__():通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
#__add__():通过重写__add__()方法，可使用自定义对象具有“+”功能
#__new__():用于创建对象
#__init__():对创建的对象进行初始化


a = 20
b = 100
c = a + b
d = a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self,other):              #若不重写，则报错 #unsupported operand type(s) for +: 'Student' and 'Student'
        return self.name + other.name
    def __len__(self):
        return len(self.name)
stu1 = Student('kaixuan')
stu2 = Student('boyu')

s = stu1 + stu2       
print(s)
s = stu1.__add__(stu2)
print(s)


lst = [10,20,30,40]
print(len(lst))
print(lst.__len__())
print(len(stu1))


 