#�̳У��﷨��ʽ   class ���������� ����1������2....��
#                      pass
#���һ����û�м̳��κ��࣬��Ĭ�ϼ̳�object
#Python֧�ֶ�̳�
#��������ʱ���������乹�캯���е��ø���Ĺ��캯��

#����
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age =age
    def info(self):
        print('name:{0},age:{1}',format(self.name,self.age))

#����
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)          #super()ֱ�����������ø���
        self.score = score

class Teacher(Person):
    def __init__(self, name, age,teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

#����
stu = Student('Jack','20','1001')
stu.info()
tea = Teacher('kaixuan','11','over')
tea.info()

#��̳�
class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass