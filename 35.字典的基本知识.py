#�ֵ䣺python���õ����ݽṹ֮һ�����б�һ����һ���ɱ�����
#�� ��ֵ�� �ķ�ʽ�洢���ݣ��ֵ���һ�� ���� ������
#�﷨��ʽ  �ֵ��� = { ... , �� : ֵ , ...}  
#�����ֵ��е�һ������ļ�ֵ�Բ���һ�����ǵ�һ��Ԫ�أ�����Ҫͨ��hash()����ͨ�������ȷ��λ��
#����hash()�����еĵļ�������һ�����ɱ�����
#�ַ������ֵ䣬Ԫ�鶼�ǲ��ɱ�����
#�ֵ��ʵ��ԭ���ֵ��ʵ��ԭ���ڲ��ֵ����ƣ����ֵ����ȸ��ݲ��׻�ƴ�����Ҷ�Ӧ��ҳ�룬python�е��ֵ��Ǹ���key����value���ڵ�λ��
#�ֵ�Ĵ�����ʹ�û�����/ʹ�����ú���dict()
#e.g: dict( name = 'jack',age = 20��

#ʹ�û�����
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print(scores,type(scores))

#�����ú���dict()
student = dict( name = 'jack',age = 20)
print(student)

#���ֵ�
d = {}
d1 = dict()
print(d)

#�ֵ�Ԫ�صĻ�ȡ
#[]   :scores['XXX']
#get():scores.get('XXX')
#���ߵ�����:[]����ֵ��в�����ָ����key���׳�keyError�쳣
#          :get()����ȡֵ������ֵ��в�����ָ����key�������׳�keyError�쳣���Ƿ���None������ͨ����������Ĭ�ϵ�value
#           �Ա�ָ����key������ʱ����

#[]
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print(scores['kaixuan'])
#print(scores['Yeah'])  ����keyError

#get()
print(scores.get('kaixuan'))
print(scores.get('Yeah'))  #None
print(scores.get('boyu',520))  #520
