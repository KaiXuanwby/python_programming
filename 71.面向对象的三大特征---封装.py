#��������������������������û�й�ϵ
#��װ����߳���İ�ȫ��
#  �����ݣ����ԣ�����Ϊ����������װ��������С��ڷ����ڲ������Խ��в��������������ⲿ���÷�����
#������������ķ����ڲ��ľ���ʵ��ϸ�ڣ��Ӷ������˸��Ӷ�
#Python��û��ר�ŵ����η��������Ե�˽�У���������Բ�ϣ����������ⲿ�����ʣ�ǰ��ʹ������"_"
#�̳У���ߴ���ĸ�����
#��̬����߳���Ŀ���չ�ԺͿ�ά����

class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('Car has opened')

car = Car('X5')
car.start()
print(car.brand)

class Student:
    def  __init__(self,name,age):
        self.name = name
        self.__age = age                 #���䲻ϣ��������ⲿʹ�ã����Լ�����_���»��ߣ�
    def show(self):
        print(self.name,self.__age)

stu = Student('kaixuan',20)
stu.show()
#������ⲿʹ��name��age
print(stu.name)
#print(stu.__age)
print(dir(stu))
print(stu._Student__age)   #������ⲿ����ͨ��  _Student__age ���з���