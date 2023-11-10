#继承：语法格式   class 子类类名（ 父亲1，父亲2....）
#                      pass
#如果一个类没有继承任何类，则默认继承object
#Python支持多继承
#定义子类时，必须在其构造函数中调用父类的构造函数

#父类
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def info(self):
        print('name:{0},age:{1}',format(self.name,self.age))

#子类
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)          #super()直接用类名调用父类
        self.score = score

class Teacher(Person):
    def __init__(self, name, age,teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

#测试
stu = Student('Jack','20','1001')
stu.info()
tea = Teacher('kaixuan','11','over')
tea.info()

#多继承
class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass