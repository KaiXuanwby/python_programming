#���õ���������
#�������ͣ�int    e.g 98
#���������ͣ�float    e.g 98.88
#�������ͣ�bool    e.g  True or False(ֻ��������ֵ)
#�ַ������ͣ�str    e.g  you are juanwang 

#�������ͣ�int��integer�� ���Ա�ʾ��������������
#�����Ĳ�ͬ���Ʊ�ʾ��ʽ
#ʮ����  Ĭ�Ͻ���  0-9
#������  ��0b��ͷ  0-1
#�˽���  ��0o��ͷ  0-7
#ʮ������  ��0x��ͷ  0-F
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

print('10:',118)
print('2:',0b10101111)#������  ��0b��ͷ
print('8:',0o176)#�˽���  ��0o��ͷ
print('16:',0x1EAF)


#���������ͣ�float
#���������������ֺ�С���������
#�������洢����ȷ
a = 3.14159
print(a,type(a))
n1 = 1.1
n2 = 2.2
print(n1+n2)
print(1.1+2.2)#ʹ�ø��������м���ʱ�����ܻ����С��λ��ȷ�������
print(1.1+2.1)#�������и�������Ӷ�����ֲ���ȷ�����
#�������������ģ��decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#�������ͣ�bool(boolean)
#������ʾ���ٵ�ֵ      True��ʾ��  False��ʾ��
#����ֵ����ת��Ϊ����    True-->1    False-->0
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
#����ֵ����ת�����������м��㣬ʹ��ʱֱ�ӵ����������мӼ�
print(f1+1)  #2��1+1��
print(f2+1)  #1��0+1��

#�ַ������ͣ�str
#�ַ����ֱ���Ϊ���ɱ���ַ�����
#����ʹ�� '������' "˫����" ''' ������'''��"""������"""������
#�����ź�˫���Ŷ�����ַ���������һ��
#�����Ŷ�����ַ������Էֲ��������Ķ���
str1 = 'Juliet and Romeo'
print(str1,type(str1))
str2 = "Juliet and Romeo"
print(str2,type(str2))
str3 = '''Juliet an
d Romeo'''
print(str3,type(str3))
str4 = """Juliet 
and Romeo"""
print(str4,type(str4))