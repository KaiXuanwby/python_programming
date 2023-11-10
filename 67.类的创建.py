#创建类的语法   class student:
#                   pass
#类的组成：类属性，实例方法，静态方法，类方法

class Student:    #Student为类的名称，简称类名。由一个或多个单词组成，每个单词的首字母要求大写，其余小写
    native_place='China'    #直接写在类里面的变量，称为类属性
    
    #初始化方法
    def __init__(self,name,age):
        self.name = name     #self,name称为实例属性，进行了一个赋值操作，将局部变量name的值赋给实例属性
        self.age = age

    #实例方法
    def eat(self):          #在类之外定义的称为函数，在类之内定义的称为方法     self为自身，要求传入一个实例方法
        print('Students are eating')

    #静态方法               静态方法只能调用类的静态属性
    @staticmethod
    def method():
        print('use staticmethod to embellish')

    #类方法                 类方法只能调用类的静态方法和静态属性，类方法的cls指的是类的元数据（类的自身）
    @classmethod
    def cm(cls):
        print('use classmethod to embellish')

#python当中一切皆对象,Student是对象吗？内存有空间吗？
print(id(Student))      #2135976075936
print(type(Student))    #<class 'type'>
print(Student)          #<class '__main__.Student'>
  