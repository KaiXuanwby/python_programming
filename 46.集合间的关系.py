#���������Ƿ���ȣ�����ʹ������� == �� ��= �����ж�
#һ�������Ƿ�����һ�����ϵ��Ӽ������Ե��÷���issubset�����ж�
#һ�������Ƿ�����һ�����ϵĳ��������Ե��÷���issuperset�����ж�
#���������Ƿ�û�н��������Ե��÷���isdisjoint�����ж�


#���������Ƿ���ȣ�Ԫ����Ⱦ����
s = {10,20,30,40}
s2 = {30,40,20,10}
print(s == s2)      #True
print(s != s2)      #False


s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.issubset(s1))  #s2��s1���Ӽ���  True
print(s3.issubset(s1))  #s3��s1���Ӽ���  False

print(s1.issuperset(s2))   #s1��s2�ĳ�����  True
print(s1.issuperset(s3))   #s1��s3�ĳ�����  False


print(s2.isdisjoint(s3))    #False   �н���ΪFalse
s4 = {100,200,300}
print(s2.isdisjoint(s4))    #True    û�н���ΪTrue