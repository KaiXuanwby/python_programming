#���ϵ���ѧ����������������������ԳƲ


#��������: intersection()��&�ȼۣ������ڽ�������
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)    
print(s1)
print(s2)


#��������: union()��|�ȼ�
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)

#�������difference()��-�ȼ�
print(s1.difference(s2))   #s1��ȥs2���Ϻ�ʣ�µ�Ԫ��
print(s1-s2)
print(s1)
print(s2)

#�ԳƲ:symmetric_difference��^�ȼ�--->A,B���ϵĲ�����ȥ����
print(s1.symmetric_difference(s2))
print(s1^ s2)
print(s1)
print(s2)
