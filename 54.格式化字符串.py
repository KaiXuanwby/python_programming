#��ʽ���ַ�������һ����ʽ������ַ���
#ʹ��%��Ϊռλ���� �ַ���%s  ����%i��%d  ������%f
#ʹ��{}��Ϊռλ��,format����

name = 'kaixuan'
age = 19
print('My name is %s , %d years this year' % (name,age))
print('My name is {0} , {1} years this year'.format(name,age))
print(f'My name is {name} , {age} years this year')

print('%10d' % 99)          #10��ʾ���ǿ��
print('%.3f' % 3.14159)     #.3��ʾ����С�������λ
print('%10.3f' % 3.14159)   #10.3�ܿ��Ϊ10��С�������λ

print('{0:.3}'.format(3.14159))   #.3��ʾ��λ��
print('{:.3f}'.format(3.14159))   #.3��ʾ��λС����0����ʡ��
print('{:10.3f}'.format(3.14159))   #.3��ʾ��λС����0����ʡ��
