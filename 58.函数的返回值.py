#�������ض��ֵʱ�����ΪԪ��

print(bool(0))
print(bool(1))

def fun(num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,34,23,44,53,55]))
#��1������û�з���ֵ������ִ�����֮�󣬲���Ҫ�����ô��ṩ���ݡ�  return����ʡ�Բ�д
#��2�������ķ���ֵ�������1����ֱ�ӷ�������
#��3�������ķ���ֵ������Ƕ�������صĽ��ΪԪ��

def fun1():
    print('hello')
fun1()

def fun2():
    return 'hello'
print(fun2())

def fun3():
    return 'hello','world'
print(fun3())

#�����ڶ���ʱ���Ƿ���Ҫ����ֵ�����������