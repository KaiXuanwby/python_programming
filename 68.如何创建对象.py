#����Ĵ����ֳ�Ϊ���ʵ����
#�﷨��  ʵ���� = ����()

class Student:    #StudentΪ������ƣ������������һ������������ɣ�ÿ�����ʵ�����ĸҪ���д������Сд
    native_place = 'China'    #ֱ��д��������ı�������Ϊ������
    
    #��ʼ������
    def __init__(self,name,age):
        self.name = name     #self,name��Ϊʵ�����ԣ�������һ����ֵ���������ֲ�����name��ֵ����ʵ������
        self.age = age

    #ʵ������
    def eat(self):          #����֮�ⶨ��ĳ�Ϊ����������֮�ڶ���ĳ�Ϊ����     selfΪ����Ҫ����һ��ʵ������
        print('Students are eating')

    #��̬����
    @staticmethod
    def method():
        print('use staticmethod to embellish')

    #�෽��
    @classmethod
    def cm(cls):
        print('use classmethod to embellish')



#����Student��Ķ���:ʵ������stu1
stu1 = Student('kaixuan',20)
stu1.eat()                               #������.������()
print(stu1.name)
print(stu1.age)

print('--------------')
Student.eat(stu1)                        #��stu1.eat()������ͬ�����ǵ���Student�е�eat����
                                         #����.������(��Ķ���)---->�������崦��self

print(id(stu1))                          #2377777937040
print(type(stu1))                        #<class '__main__.Student'>
print(stu1)                              #<__main__.Student object at 0x000002299E9BFA90>
#ʵ������������ָ��ָ�������   �����Student    ʵ������stu1����������󴴽�������





#���壺����ʵ�����Ϳ��Ե������е�����



