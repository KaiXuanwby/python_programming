#python�Ƕ�̬���ԣ��ڴ�������֮�󣬿��Զ�̬�İ����Ժͷ���

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name,'is eating dinner')

stu1 = Student('kaixuan',20)                  
stu2 = Student('boyu',21)

#Ϊstu2��̬�İ��Ա�����
stu2.gender = 'fem'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

stu1.eat()
stu2.eat()
Student.eat(stu1)
Student.eat(stu2)

def show():
    print('I`m outside, you can call me function ')
#Ϊstu1��̬�󶨷���
stu1.show=show
show()
stu1.show()
#stu2.show()    ����