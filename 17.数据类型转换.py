#��������ת����Ϊʲô��Ҫ��������ת����
#����ͬ�������͵�����ƴ����һ��
name = 'a'
age = 20

print(type(name),type(age))#�������Ͳ���ͬ
print('My name is ',name,'I\'m ',age,' years old')
#print('My name is '+name+'I\'m '+age+' years old')#ִ�к󱨴�can only concatenate str (not "int") to str
#�������Խ��ַ���str��int�����üӺŽ������ӣ�
#��+�� ��Ϊ���ӷ�
#�������������ת��
print('My name is '+name+'I\'m '+str(age)+' years old')#��int����ͨ��str()ת������str����

#str()   int()   float()


#str()������������ת��Ϊstr,Ҳ����������ת��   e.g����123��

a = 10
b = 198.5
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))#ת��ʱ�൱���βα��������ƣ���ֻ�ı䵱�²��ı䱾��
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

#int()������������ת��Ϊint

s1  = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))#��strת��int���ͣ��ַ�����Ϊ���ִ�
print(int(f1),type(int(f1)))#��floatת��int���ͣ���ȡ�������֣����С������
#print(int(s2),type(int(s2))) ������strת��int���ͣ���Ϊ�ַ���ΪС����
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3)))  ������strת��int����ʱ���ַ�������Ϊ���ִ����������������ִ�������ת��

#float()������������ת��Ϊfloat
s1  = '128.98'
s2 = '76'
ff = True
s3 = 'hello'
i = 98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))   �����ַ����е���������Ƿ��ַ�����������ת��
print(float(i),type(float(i)))