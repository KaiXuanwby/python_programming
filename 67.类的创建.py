#��������﷨   class student:
#                   pass
#�����ɣ������ԣ�ʵ����������̬�������෽��

class Student:    #StudentΪ������ƣ������������һ������������ɣ�ÿ�����ʵ�����ĸҪ���д������Сд
    native_place='China'    #ֱ��д��������ı�������Ϊ������
    
    #��ʼ������
    def __init__(self,name,age):
        self.name = name     #self,name��Ϊʵ�����ԣ�������һ����ֵ���������ֲ�����name��ֵ����ʵ������
        self.age = age

    #ʵ������
    def eat(self):          #����֮�ⶨ��ĳ�Ϊ����������֮�ڶ���ĳ�Ϊ����     selfΪ����Ҫ����һ��ʵ������
        print('Students are eating')

    #��̬����               ��̬����ֻ�ܵ�����ľ�̬����
    @staticmethod
    def method():
        print('use staticmethod to embellish')

    #�෽��                 �෽��ֻ�ܵ�����ľ�̬�����;�̬���ԣ��෽����clsָ�������Ԫ���ݣ��������
    @classmethod
    def cm(cls):
        print('use classmethod to embellish')

#python����һ�нԶ���,Student�Ƕ������ڴ��пռ���
print(id(Student))      #2135976075936
print(type(Student))    #<class 'type'>
print(Student)          #<class '__main__.Student'>
  