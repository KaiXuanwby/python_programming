#������д���������Լ̳и����ĳ�����Ի򷽷������⣬�����������ж��䣨�����壩�������±�д
#������д��ķ����п���ͨ��super().xxx()���ø����б���д�ķ���

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print('name:{0},age:{1}'.format(self.name,self.age))

#��������
class Student(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def info(self):
        super().info()
        print('number:{0}'.format(self.score))

#����
stu = Student('Jack',20,'1001')
stu.info()



