#���ϵ���ز���

#����Ԫ�ص��жϲ�����in  /   not in
s = {10,20,30,40,50}
print(10 in s)         #True
print(100 in s)        #False
print(10 not in s)     #False
print(100 not in s)    #True


#����Ԫ�ص���������������add()������һ�����һ��Ԫ��
#                    ����update()�����������һ��Ԫ��
s.add(80)
print(s)
s.update({200,400,300})
print(s)
s.update([100,99,8])
print(s)
s.update((78,64,56))
print(s)

#����Ԫ�ص�ɾ������������remove()��һ��ɾ��һ��ָ��Ԫ�أ����ָ����Ԫ�ز������׳�KeyError
#                    ����discard(),һ��ɾ��һ��ָ��Ԫ�أ����ָ����Ԫ�ز����ڲ��׳��쳣
#                    ����pop(),һ��ֻɾ��һ������Ԫ��
#                    ����clear()��������ռ���
s.remove(100)
print(s)
#s.remove(500)       #KeyError:500
#print(s)
s.discard(500)       #������
print(s)
s.pop()              #ɾ�������Ǽ��ϵĵ�һ��Ԫ�أ�hash�����
print(s)
#s.pop(400)          #pop��������Ӳ�����ֻ��д�޲����ģ�д������ᱨ��
s.clear()
print(s)
