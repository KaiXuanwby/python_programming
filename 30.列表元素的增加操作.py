#�б�Ԫ�ص����Ӳ���
#append()�����б��ĩβ���һ��Ԫ��
#extend()�����б��ĩβ�������һ��Ԫ��
#insert()�����б������λ�����һ��Ԫ��
#��Ƭ�����б������λ���������һ��Ԫ��

lst = [10,20,30]
print('before',lst,id(lst))
lst.append(100)
print('after',lst,id(lst))
lst2 = ['hello','world']
lst.append(lst2)   #��lst2��Ϊһ��Ԫ����ӵ��б��ĩβ
print(lst)
lst.extend(lst2)
#���б��ĩβһ������Ӷ��Ԫ��
print(lst)

lst.insert(1,90)  #��90���Ԫ����ӵ�����Ϊ1�ĵط�ȥ
print(lst)

lst3 = [True,False,'hello']
#lst[1:] = lst3
lst[1:1] = lst3
print(lst)


