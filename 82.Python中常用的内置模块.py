#ģ����
#sys����python���������价��������صı�׼��
#time���ṩ��ʱ����صĸ��ֺ����ı�׼��
#os���ṩ�˷��ʲ���ϵͳ�����ܵı�׼��
#calendar���ṩ��������صĸ��ֺ����ı�׼��
#urllib�����ڶ�ȡ�������ϣ��������������ݱ�׼��
#json������ʹ��JSON���л��ͷ����л�����
#re���������ַ�����ִ��������ʽƥ����滻
#math���ṩ��׼�������㺯���ı�׼��
#decimal�����ڽ��о�ȷ�������㾫�ȡ���Ч��λ���������������ʮ��������
#logging���ṩ�����ļ�¼�¼������󡢾���͵�����Ϣ����־��Ϣ�Ĺ���

import sys
import time
import urllib.request
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())



