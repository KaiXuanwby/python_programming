#input����
#���ã����������û�������
#����ֵ���ͣ�����ֵ������Ϊstr
#ֵ�Ĵ洢��ʹ��=�������ֵ���д洢
present=input('What do you want?')
print(present,type(present))

#�Ӽ���¼�������������������������ĺ�
n1 = input('Please enter a number(this number will be uesd to add)')
n2 = input('Please enter another number(this number will be uesd to add)')
print(n1+n2)#�ñ��ʽû�н��мӷ�����������������ã�ԭ��Ϊ����ֵ������Ϊstr����Ҫ����ת��
print(type(n1),type(n2))
#�������
#��1
print(int(n1)+int(n2))
#��2
n1 = int(n1)
n2 = int(n2)
print(n1+n2)
#��3
a = int(input('Please enter a number(this number will be uesd to add)'))
b = int(input('Please enter another number(this number will be uesd to add)'))
print(a+b)