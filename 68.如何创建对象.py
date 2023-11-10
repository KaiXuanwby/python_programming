#对象的创建又称为类的实例化
#语法：  实例名 = 类名()

class Student:    #Student为类的名称，简称类名。由一个或多个单词组成，每个单词的首字母要求大写，其余小写
    native_place = 'China'    #直接写在类里面的变量，称为类属性
    
    #初始化方法
    def __init__(self,name,age):
        self.name = name     #self,name称为实例属性，进行了一个赋值操作，将局部变量name的值赋给实例属性
        self.age = age

    #实例方法
    def eat(self):          #在类之外定义的称为函数，在类之内定义的称为方法     self为自身，要求传入一个实例方法
        print('Students are eating')

    #静态方法
    @staticmethod
    def method():
        print('use staticmethod to embellish')

    #类方法
    @classmethod
    def cm(cls):
        print('use classmethod to embellish')



#创建Student类的对象:实例对象stu1
stu1 = Student('kaixuan',20)
stu1.eat()                               #对象名.方法名()
print(stu1.name)
print(stu1.age)

print('--------------')
Student.eat(stu1)                        #与stu1.eat()意义相同，都是调用Student中的eat方法
                                         #类名.方法名(类的对象)---->方法定义处的self

print(id(stu1))                          #2377777937040
print(type(stu1))                        #<class '__main__.Student'>
print(stu1)                              #<__main__.Student object at 0x000002299E9BFA90>
#实例对象中有类指针指向类对象   类对象：Student    实例对象：stu1，根据类对象创建出来的





#意义：有了实例，就可以调用类中的内容



