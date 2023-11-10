# coding=utf-8
# 类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
# 类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
# 静态方法：使用@staticmethod修饰的主法，使用类名直接访问的方法

class Student:    # Student为类的名称，简称类名。由一个或多个单词组成，每个单词的首字母要求大写，其余小写
    
    native_place = 'China'    # 直接写在类里面的变量，称为类属性
    
    # 初始化方法
    def __init__(self, name, age):
        self.name = name     # self,name称为实例属性，进行了一个赋值操作，将局部变量name的值赋给实例属性
        self.age = age

    # 实例方法
    def eat(self):          # 在类之外定义的称为函数，在类之内定义的称为方法     self为自身，要求传入一个实例方法
        print('Students are eating')

    # 静态方法                        静态方法只能调用类的静态属性
    @staticmethod
    def method():
        print('use staticmethod to embellish')

    # 类方法                          类方法只能调用类的静态方法和静态属性，类方法的cls指的是类的元数据（类的自身）
    @classmethod
    def cm(cls):
        print('use class_method to embellish')


# 类属性的使用方式：使用类名调用
print(Student.native_place)
stu1 = Student('kai_xuan', 20)                  # 每一个对象都开辟一个新的内存空间
stu2 = Student('bo_yu', 21)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = 'ShanXi'
print(stu1.native_place)
print(stu2.native_place)

# 类方法的使用方式
Student.cm()
stu1.cm()
# 静态方法的使用方法
Student.method()
stu1.method()
# 类方法与静态方法的区别
# 访问权限：类方法可以访问和修改类属性，也可以调用其他的类方法和静态方法。
#          静态方法无法访问或修改类属性，也无法调用其他的类方法和静态方法。
# 对象绑定：类方法是绑定到类而非实例的，因此可以通过类直接调用类方法。
#          而静态方法不与类或实例绑定，因此可以通过类或实例调用静态方法。


class MyClass:
    class_attr = 10

    @classmethod
    def class_method(cls):
        print("Class method")
        print("class_attr:", cls.class_attr)  # 可以访问类属性
        cls.class_attr = 20  # 可以修改类属性

    @staticmethod
    def static_method():
        print("Static method")
        # print("class_attr:", cls.class_attr)  # 静态方法无法访问类属性
        # cls.class_attr = 20  # 静态方法无法修改类属性


# 通过类调用类方法
MyClass.class_method()

# 通过类调用静态方法
MyClass.static_method()

# 通过实例调用类方法和静态方法
obj = MyClass()
obj.class_method()
obj.static_method()
