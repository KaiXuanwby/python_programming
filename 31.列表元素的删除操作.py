#�б�Ԫ�ص�ɾ������
#remove(): һ��ɾ��һ��Ԫ��;�ظ�Ԫ��ֻɾ����һ��;Ԫ�ز������׳�ValueError
#pop(): ɾ��һ��ָ������λ���ϵ�Ԫ��;ָ�������������׳�IndexError;�����ָ��������ɾ���б������һ��Ԫ��
#��Ƭ: һ������ɾ��һ��Ԫ��
#clear(): ����б�
#del: ɾ���б�

lst = [10,20,30,40,50,60,30]
lst.remove(30)
print(lst)

lst.pop(1)
print(lst)
lst.pop()
print(lst)

new_lst = lst[1:3]  #�������µ��б����,ԭ�б�û�б�
print('before',lst)
print('after',new_lst)
print(id(lst),id(new_lst))

#�������µ��б���󣬶���ɾ���б��е�����
lst[1:3] = []
print(lst)
print(id(lst))

lst.clear
print(lst)

del lst
#print(lst) ����



