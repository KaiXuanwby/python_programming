#Ԫ�飺python���õ����ݽṹ֮һ����һ�����ɱ�����
#�������У��ַ�����Ԫ��
#  �������У�û������ɾ���ĵĲ���
#�ɱ����У��б��ֵ�
#  �ɱ����У����Զ�����ִ������ɾ���Ĳ����������ַ����������

lst = [10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
print(s)

#Ԫ�飺 ( Ԫ�ض��� , Ԫ�ض��� , ...)
#Ԫ��Ĵ�����ʽ��
#ֱ��С���ţ�  t = ('python','hello',90)
#���ú���tuple:   t = tuple(('python','hello',90))
#ֻ����һ��Ԫ�ص�Ԫ����Ҫʹ�ö��ź�С����:   t = (10,)

t = ('python','hello',90)
print(t,type(t))

t1 = 'python','hello',90
print(t1,type(t1))

t2 = ('python',)   #���Ԫ����ֻ��һ��Ԫ�أ����Ų���ʡ
print(t2,type(t2))

t3 = tuple(('python','hello',90))
print(t3,type(t3))

#��Ԫ��Ĵ�����ʽ
t4 = ()
t5 = tuple()