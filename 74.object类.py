#object��
#object����������ĸ��࣬��������඼��object������Ժͷ�����
#���ú���dir()���Բ鿴ָ��������������
#object��һ��__str__()���������ڷ���һ������"���������"����Ӧ�����ú���str()��������print()�����������ǲ鿴�������Ϣ
#�������__str__()������д

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


