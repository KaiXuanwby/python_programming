#��̬���򵥵�˵����̬���ǡ����ж�����̬������ָ���ǣ����㲻֪��һ�����������õĶ��󵽵���ʲô���ͣ�
#��Ȼ����ͨ������������÷����������й����и��ݱ��������ö�������ͣ���̬���������ĸ������еķ���

class Animal(object):                 #object����ʡ��
    def eat(self):
        print('Animals need to eat')
class Dog(Animal):
    def eat(self):
        print('Dog eats meat')
class Cat(Animal):
    def eat(self):
        print('Cats eat fishes')
class Person(object):                   #object����ʡ��
    def eat(self):
        print('People eat foods')

def fun(a):
    a.eat()

fun(Dog())
fun(Cat())
fun(Person())
fun(Animal())

#��̬�����붯̬���Թ��ڶ�̬������
#��̬����ʵ�ֶ�̬��������Ҫ����
#�̳У���������������ָ���������

#��̬���ԵĶ�̬���С�Ѽ�����͡�������һֻ����������Ѽ�ӡ���Ӿ������Ѽ�ӡ�������Ҳ��Ѽ�ӣ���ô��ֻ��Ϳ��Ա���ΪѼ��
#��Ѽ�������У�����Ҫ���Ķ�����ʲô���ͣ������ǲ���Ѽ�ӣ�ֻ���Ķ������Ϊ