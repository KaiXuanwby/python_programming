#������������
#��������ܷ��ʸñ���������
#���ݱ�����Ч��Χ�ɷ�Ϊ
#�ֲ��������ں����ڶ��岢ʹ�õı�����ֻ�ں����ڲ���Ч���ֲ�����ʹ��global��������������ͻ���ȫ�ֱ���
#ȫ�ֱ������������ⶨ��ı������������ں�������

def fun(a,b):
    c=a+b           #cΪ�ֲ�����
    print(c)

name = 'kaixuan'    #nameΪȫ�ֱ���
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age     #global����:�ֲ������ͻ���ȫ�ֱ���
    age = 20
    print(age)
fun3()
print(age)
