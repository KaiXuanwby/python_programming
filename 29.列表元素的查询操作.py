#�б�Ԫ�صĲ�ѯ����
#��ȡ�б��еĶ��Ԫ��
#�﷨��ʽ���б���[ start : stop : step]
#��Ƭ�Ľ����ԭ�б�Ƭ�εĿ���

#��Ƭ�ķ�Χ��[start:stop]

#stepĬ��Ϊ1 ����дΪ[start:stop]

#stepΪ����-->[:stop:step]-->��Ƭ�ĵ�һ��Ԫ��Ĭ�����б�ĵ�һ��Ԫ��-->��start��ʼ���������Ƭ
#         |-->[start::step]-->��Ƭ�����һ��Ԫ��Ĭ�����б�����һ��Ԫ��-->��start��ʼ���������Ƭ

#stepΪ����-->[:stop:step]-->��Ƭ�ĵ�һ��Ԫ��Ĭ�����б�����һ��Ԫ��-->��start��ʼ��ǰ������Ƭ
#         |-->[start::step]-->��Ƭ�����һ��Ԫ��Ĭ�����б�ĵ�һ��Ԫ��-->��start��ʼ��ǰ������Ƭ

lst = [10,20,30,40,50,60,70,80]
#print(lst[1:6:1])  #�µ��б����
print('before',id(lst))
lst2 = lst[1:6:1]
print('after',id(lst2))
print(lst[1:6])   #stepĬ��Ϊ1
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])

print(lst[::-1])    #�������Ԫ��
print(lst[7::-1])
print(lst[6:0:-2])


#�ж�ָ��Ԫ�����б����Ƿ����
#Ԫ�� in �б���
#Ԫ�� not in �б���
#�б�Ԫ�صı���
#for �������� in �б���

print('p' in 'python')  #True
print('k' not in 'python')  #True

lst = [10,20,'python','hello']
print(10 in lst)   #True
print(100 in lst)   #False
print(10 not in lst)   #False
print(100 not in lst)   #True
#��������б�Ԫ��
for item in lst:
    print(item)