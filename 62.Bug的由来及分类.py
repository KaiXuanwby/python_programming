#Debug:���bug
#SyntaxError�����ĵ��µ��﷨����

age = input('Please enter your age:')    
print(type(age))
#if age >= 18:
if int(age) >= 18:
    print('you are adult')

i = 0
while i<10:
        print(i)
        i +=1

#��������
#©��ĩβ��ð�ţ���if��䣬ѭ�����,else���
#��������
#��Ӣ�ķ���д�����ķ���
#�ַ���ƴ�ӵ�ʱ�򣬰��ַ���������ƴ��һ��
#û�ж������������˵whileѭ���ı���
#��==���͡�=�����������


#֪ʶ�㲻�������µĴ���
#IndexError:����Խ������
lst = [11,22,33,44]
#print(lst[4])       #IndexError
print(lst[3])
#append()�������ղ�����
lst = []
#lst = append('A','B','C')  append����һ��ֻ�����һ��Ԫ��
lst.append('A')     
print(lst)

#˼·���嵼�µ�����������
#ʹ��print()����
#ʹ��#��ʱע�͵����ִ���

#�������������µ��쳣����������߼�û�д�ֻ����Ϊ�û������������һЩ������������µĳ������
#��������쳣������ƣ����쳣����ʱ��ʹ����
#    try:
#       ���ܻ�����쳣�Ĵ���
#    except �쳣����:
#       �쳣������루�����ִ�еĴ��룩

try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
    print('result is ',result)
except ZeroDivisionError :
    print('Sorry, zero is unacceptable')
print('over')

#���except�ṹ�������쳣��˳��������������˳��Ϊ�˱�����©���ܳ��ֵ��쳣���������������BaseException
#    try:
#       ���ܻ�����쳣�Ĵ���
#    except �쳣����1:
#       �쳣������루�����ִ�еĴ��룩
#    except �쳣����2:
#       �쳣������루�����ִ�еĴ��룩
#    ......
#    except BaseException:
#       �쳣������루�����ִ�еĴ��룩

try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
    print('result is ',result)
except ZeroDivisionError :
    print('Sorry, zero is unacceptable')
    print('over')
except ValueError :
    print('cannot change str to number')
except BaseException as e:
    print(e)


#try...except...else�ṹ
#���try����û���׳��쳣����ִ��else�飬���try���׳��쳣����ִ��except��
try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
except BaseException as e:             #�Ѵ������e,����������������ԭ��
    print('Wrong!')
    print(e)
else:    
    print('result is ',result)


#try...except...else...finally�ṹ
#finally���������Ƿ����쳣���ᱻִ�еĴ��룬�ܳ������ͷ�try�����������Դ
try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
except BaseException as e:             #�Ѵ������e,����������������ԭ��
    print('Wrong!')
    print(e)
else:    
    print('result is ',result)
finally:
    print('Programm is over, thanks')