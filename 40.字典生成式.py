#�ֵ�����ʽ:{ ��ʾ�ֵ�key�ı��ʽ : ��ʾ�ֵ�value�ı��ʽ for �Զ����ʾkey�ı���,�Զ����ʾvalue�ı��� in �ɵ������� }
#���ú���zip()
#���ڽ��ɵ���������Ϊ�������������ж�ӦԪ�ش����һ��Ԫ�飬Ȼ�󷵻�����ЩԪ����ɵ��б�


items = ['Firuts','Books','Others']
prices = ['96','78','85']       #��ֵ���ڼ�����ֻȡǰ��

d = {item.upper():price for item , price in zip(items,prices)}  #upper��items�еĶ���ȫ��ת��Ϊ��д
print(d)




