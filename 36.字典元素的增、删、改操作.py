#key���жϣ�
#in    :ָ����key���ֵ��д��ڷ���True-->'XXX' in scores
#not in:ָ����key���ֵ��в����ڷ���True-->'XXX' not in scores

#�ֵ�Ԫ�ص�ɾ��
# del scores['XXX']

#�ֵ�Ԫ�ص�����
# scores['XXX'] = XXX

#�����ж�
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print('Bob' in scores)
print('Bob' not in scores)

del scores['Bob']
print(scores)
#scores.clear()

scores['jianghaowen'] = 98   #�ֵ�Ԫ�ص�����
print(scores)
