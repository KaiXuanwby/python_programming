#�б�Ԫ�ص����������
#����sort()�������б��е�����Ԫ��Ĭ�ϰ���С�����˳��������У�����ָ��reverse = True,���н������򣬲������µ��б����ԭ�б��

lst = [20,40,10,98,54]
print('before',lst,id(lst))
lst.sort()
print('after',lst,id(lst))  #id��ͬ��˵������ԭ�б�Ļ����Ͻ�������

#����
lst.sort(reverse = True)   #reserve = FalseΪ��������
print(lst,id(lst))


#�������ú���sorted()������ָ��reverse = True,���н�������ԭ�б������ı�,�����µ��б����ԭ�б���
lst = [20,40,10,98,54]
print('before',lst,id(lst))
new_lst = sorted(lst)   #sorted��ԭ�б��Ԫ���ź���Ȼ��ŵ�һ�����б���
print(new_lst,id(new_lst))
desc_lst = sorted(lst,reverse = True)
print(desc_lst,id(desc_lst))
