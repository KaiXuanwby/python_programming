#���룺���ַ���ת��Ϊ���������ݣ�bytes��
#���룺��bytes���͵�����ת�����ַ�������

s = 'today'
print(s.encode(encoding = 'GBK'))  #GBK�����ʽ��һ������ռ�����ֽ�
print(s.encode(encoding = 'UTF-8'))  #UTF-8�����ʽ��һ������ռ�����ֽ�
#��ͬ�ı����ʽ����ռ���ֽ���

#byte����ľ���һ�����������ݣ��ֽ����͵����ݣ�
byte = s.encode(encoding = 'GBK')
print(byte.decode(encoding = 'GBK'))

byte = s.encode(encoding = 'UTF-8')
print(byte.decode(encoding = 'UTF-8'))
#����ͽ���ĸ�ʽһ��Ҫ��ͬ


