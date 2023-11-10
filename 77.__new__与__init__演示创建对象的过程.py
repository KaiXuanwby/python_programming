# coding=utf-8
# __new__():用于创建对象
# __init__():对创建的对象进行初始化

class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__ has been used, cls is{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('the thing which has been created id is:{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__ has been uesd, the id of self is {0}'.format(id(self)))
        self.name = name
        self.age = age


print('the id of object is {0}'.format(id(object)))
print('the id of Person is {0}'.format(id(Person)))

# 创建Person类的实例对象
p1 = Person('kaixuan', 20)
print('the id of p1 is {0}'.format(id(p1)))

# 解释：在前面的案例中，如果在类中没有显式地对__new__方法进行重写，
# Python会默认调用父类object的__new__方法来创建实例对象，这就是一般情况下实例对象的创建。
# 在本节代码中，相当于对父类的object里的__new__()方法进行重写，为了更加显性的看到对象究竟是怎样创建的
# 在重写的过程中，通过id来观察对象的创建与传递
# 创建对象：p1 = Person('kaixuan',20)
# 第一步:Person 传递到 def __new__(cls,*args,**kwargs):中的cls
# 第二步:cls 传递到 obj = super().__new__(cls) 中的cls，该式有两个作用，一是对父类new进行重写的声明
#      二是创建一个新的对象obj
# 第三步:obj传递到 def __init__(self,name,age): 中的self位置，对象创建完毕
# 最后，通过id可以看到   obj就是p1 , cls就是Person
