#ģ���Ӣ��ΪModules
#������ģ��Ĺ�ϵ��һ��ģ����԰���n�������
#��Python��һ����չ��Ϊ.py���ļ�����һ��ģ��
#ʹ��ģ��ĺô���������������ͽű��ĵ��벢ʹ��
#                ���⺯�������������ͻ
#                ��ߴ���Ŀ�ά����
#                ��ߴ���Ŀ�������
#ģ���а����������࣬���

#����ģ��
#import ģ������ [as ����]
#from ģ������ import ����/����/��
import math              #������ѧ����
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-------------------------------')
print(dir(math))                            #�۲�mathģ��������Щ����
print(math.pow(2,3),type(math.pow(2,3)))    #pow(a,b)a��b����
print(math.ceil(9.001))                     #ceil����ȡ��
print(math.floor(9.9999))                   #����ȡ��

#��ֻ��ʹ��math���е�pi����������д
from math import pi
print(pi)
print(pow(2,3))                              #����ʹ�ã�buitinsģ�飩����ֵΪint
print(math.pow(2,3))                         #math����(mathģ��) ����ֵΪfloat

from math import pow
print(pow(2,3))

#�Զ���ģ��ĵ���
import calculation
print(calculation.add(10,20))
print(calculation.div(10,20))

from calculation import add
print(add(10,20))