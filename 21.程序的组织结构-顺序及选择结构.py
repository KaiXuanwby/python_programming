#�κμ򵥻��ӵ��㷨��������˳��ṹ��ѡ��ṹ��ѭ���ṹ�����ֻ����ṹ��϶���
#˳��ṹ
#ѡ��ṹ��if���
#ѭ���ṹ: while���     for-in���


#˳��ṹ��������ϵ���ִ�д��룬�м�û���κ��жϺ���ת��ֱ���������
print('---------- start ----------')
print('open the door')
print('put the things to it')
print('close the door')
print('---------- end ----------')#ͨ����Ӷϵ��������۲�

#����Ĳ���ֵ
#python ��һ�нԶ������ж�����һ������ֵ
#��ȡ����Ĳ���ֵ��ʹ�����ú���bool()
#��Щ����Ĳ���ֵΪFalse��False ��ֵ0��None,���ַ��������б���Ԫ�飬���ֵ䣬�ռ���
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#���б�
print(bool(list()))#���б�
print(bool(()))#��Ԫ��
print(bool(tuple()))#��Ԫ��
print(bool({}))#���ֵ�
print(bool(dict()))#���ֵ�
print(bool(set()))#�ռ���
#�������������⣬�������Ĳ���ֵ��ΪTrue


#ѡ��ṹ�������ж������Ĳ���ֵѡ���Ե�ִ�в��ִ��롣��ȷ���ü����֪����ʲô�����£���ȥ��ʲô
#����֧�ṹ���������壺���...��...
#"""�﷨�ṹ��if+�������ʽ+:
#                 ����ִ����
#"""
#���������ʽ�������д���ʽ������ֱ������һ��ֵ���߱�����������ٵ��жϽ����������ֵ���߱����Ĳ���ֵ�����ж�
money = 1000
s = float(input('How much money would you want to take?'))
if money>=s:
    money-=s
    print('It has been token successfully!\n you still have',money,'money')

#˫��֧�ṹ���������壺���...��...������...��...
#�﷨�ṹ��if+�������ʽ+:
#             ����ִ����1
#          else+:
#             ����ִ����2
num = int(input('Please enter an integer number:'))

if num%2==0:
    print('num is an even number.\t',num)
else:
    print('num is an uneven/odd number.\t',num)


#���֧�ṹ
#�﷨�ṹ��if+�������ʽ1+:
#             ����ִ����1
#          elif+�������ʽ2+:
#             ����ִ����2
#          elif+�������ʽ3+:
#             ����ִ����3
#            ..............
#          [else:]         ----->  ��д�ɲ�д
#             ����ִ����N

grade = int(input('please enter your grade'))
if   grade<=100 and grade>=90:             #�˴��ɸ�дΪ90<=grade<=100
    print('You has got the A standard.')
elif grade<90 and grade>=80:               #�˴��ɸ�дΪ80<=grade<=89
    print('You has got the B standard.')
elif grade<80 and grade>=70:               #�˴��ɸ�дΪ70<=grade<=79
    print('You has got the C standard.')
elif grade<70 and grade>=60:               #�˴��ɸ�дΪ60<=grade<=69
    print('You has got the D standard.')
elif grade<60 and grade>0:                 #�˴��ɸ�дΪ0<=grade<=59
    print('You has got the E standard.')
else:
    print('Your grade is illegal,try again.')


#Ƕ��if
#�﷨�ṹ��if+�������ʽ1:
#              if+�ڲ��������ʽ��
#                  �ڲ�����ִ����1
#              else:
#                  �ڲ�����ִ����2
#          else:
#              ����ִ����

membership = int(input('Are you a member of our store?\nIf you are,please enter 1.\nIf you aren\'t,please eneter 0'))
consumption  = float(input('How much things did you cost? '))
if membership==1:
    if consumption>=200:
        consumption *= 0.8
    elif 100<=consumption<200:
        consumption *= 0.9
    else:
        consumption=consumption
elif membership==0:
    if consumption>=200:
        consumption *= 0.95
    else:
        consumption = consumption

print('Your consumption is',consumption)

#�������ʽ��if...else�ļ�д
#�﷨�ṹ��   x  if  �ж�����  else  y
#�������;����ж������Ĳ���ֵΪTrue,�������ʽ�ķ���ֵΪx�������������ʽ�ķ���ֵΪFalse

num1 = int(input('Please enter the first number:'))
num2 = int(input('Please enter the second number:'))

#"""
if num1 >= num2:
    print(num1,'>=',num2)
else:
    print(num1,'<',num2)
#"""

print(   str(num1)+'>='+str(num2)   if num1 >= num2 else   str(num1)+'<'+str(num2)   )

#pass���
#pass���ʲô��������ֻ��һ��ռλ���������﷨����Ҫ���ĵط�
#ʲôʱ��ʹ�ã��ȴ�﷨�ṹ����û��ô�����ôд��ʱ��
#��Щ���һ��ʹ�ã�if��������ִ����
#                  for-in����ѭ����
#                  ���庯���ĺ�����