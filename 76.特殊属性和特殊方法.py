#�������Ժͷ������������»��߿�ʼ�����»��߽������ͳ�Ϊ��������Ի��߷���
#�������ԣ�
#__dict__:���������ʵ���������󶨵��������Ժͷ������ֵ�

#print(dir(object))


class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
#����C��Ķ���
x = C('Jack',20)     #x��C���͵�һ��ʵ������
print(x.__dict__)    #��ӡ���Ϊʵ������������ֵ䣬�õ�һ���ֵ䣬���������Ϊ�������������ֵΪ�ֵ䵱�е�һ��ֵ
print(C.__dict__)    #���Ϊ���������Կ��������Ժͷ�����ɵ��ֵ�
print(x.__class__)   #���������������
print(C.__bases__)   #������Ǹ���������ɵ�Ԫ��
print(C.__base__)    #������Ǻ�C�������ĸ��ࣨ��һ��
print(C.__mro__)     #�����Ĳ�νṹ
print(A.__subclasses__())   #������б�



#���ⷽ����
#__len__():ͨ����д__len__()�����������ú���len()�Ĳ����������Զ�������
#__add__():ͨ����д__add__()��������ʹ���Զ��������С�+������
#__new__():���ڴ�������
#__init__():�Դ����Ķ�����г�ʼ��


a = 20
b = 100
c = a + b
d = a.__add__(b)
print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = name
    def __add__(self,other):              #������д���򱨴� #unsupported operand type(s) for +: 'Student' and 'Student'
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


 