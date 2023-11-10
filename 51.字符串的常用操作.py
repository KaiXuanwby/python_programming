#�ַ����Ĳ�ѯ����
#index():�����Ӵ�substr��һ�γ��ֵ�λ�ã�������ҵ��Ӵ������ڣ����׳�ValueError
#rindex():�����Ӵ�substr���һ�γ��ֵ�λ�ã�������ҵ��Ӵ������ڣ����׳�ValueError
#find():�����Ӵ�substr��һ�γ��ֵ�λ�ã�������ҵ��Ӵ������ڣ��򷵻�-1
#rfind():�����Ӵ�substr���һ�γ��ֵ�λ�ã�������ҵ��Ӵ������ڣ��򷵻�-1
#�ַ���������ģ�������
s = 'hello,hello'
print(s.index('lo'))     #3
print(s.find('lo'))      #3
print(s.rindex('lo'))    #9     
print(s.rfind('lo'))     #9

'''
     <-----------------------------
    -11-10-9 -8 -7 -6 -5 -4 -3 -2- 1
     h  e  l  l  o  ,  h  e  l  l  o
     0  1  2  3  4  5  6  7  8  9 10
     -------------------------------->
'''

#print(s.index('k'))     #ValueError:substring not found
print(s.find('k'))      #-1
#print(s.rindex('k'))    #ValueError:substring not found 
print(s.rfind('k'))     #-1



#�ַ����Ĵ�Сдת����ʽ
#upper():���ַ����������ַ�ת��Ϊ��д��ĸ
#lower():���ַ����������ַ�ת��ΪСд��ĸ
#swapcase():���ַ��������д�д�ַ�ת��ΪСд��ĸ�����ַ���������Сд�ַ�ת��Ϊ��д��ĸ
#capitalize():�ѵ�һ���ַ�ת��Ϊ��д������ת��ΪСд
#title():��ÿ�����ʵ�һ���ַ�ת��Ϊ��д��ÿ�����ʵ�ʣ���ַ�ת��ΪСд

s = 'hello,python'
a = s.upper()
print(a,id(a))
print(s,id(s))
b = s.lower()
print(b,id(b))
print(s,id(s))
print(b == s)
print(b is s)

s2 = 'Hello,Python'
print(s2.swapcase())
print(s2.capitalize())

s3 = 'i love you'
print(s3.title())



#�ַ������ݶ�������ķ���
#center():���ж��룬��һ������ָ����ȣ��ڶ�������ָ���������ڶ��������ǿ�ѡ�ģ�Ĭ���ǿո�������ÿ��С��ʵ�ʿ���򷵻�ԭ�ַ���
#ljust():����룬��һ������ָ����ȣ��ڶ�������ָ���������ڶ��������ǿ�ѡ�ģ�Ĭ���ǿո�������ÿ��С��ʵ�ʿ���򷵻�ԭ�ַ���
#rjust():�Ҷ��룬��һ������ָ����ȣ��ڶ�������ָ���������ڶ��������ǿ�ѡ�ģ�Ĭ���ǿո�������ÿ��С��ʵ�ʿ���򷵻�ԭ�ַ���
#zfill():�Ҷ��룬�����0��䣬�÷���ֻ����һ������������ָ���ַ����Ŀ�ȣ����ָ���Ŀ��С�ڵ����ַ����ĳ��ȣ������ַ�������

s = 'hello,Python'
print(s.center(20,'*'))

print(s.ljust(20,'*'))
print(s.ljust(10))
print(s.ljust(20))

print(s.rjust(20,'*'))
print(s.rjust(10))
print(s.rjust(20))

print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))  #����ǰ���0

#�ַ������ֲ����İ취
#split():���ַ�������߿�ʼ���֣�Ĭ�ϵ������ַ��ǿո��ַ��������ص�ֵ����һ���б�
#        :��ͨ������sepָ���������ַ��������ַ�
#        :ͨ������maxsplitָ�������ַ���ʱ��������ִ������ھ����������֮��ʣ����ִ��ᵥ����Ϊһ����
#rsplit()::���ַ������ұ߿�ʼ���֣�Ĭ�ϵ������ַ��ǿո��ַ��������ص�ֵ����һ���б�
#        :��ͨ������sepָ���������ַ��������ַ�
#        :ͨ������maxsplitָ�������ַ���ʱ��������ִ������ھ����������֮��ʣ����ִ��ᵥ����Ϊһ����

s = 'hello world python'
lst = s.split()
print()
s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

print(s.rsplit())
print(s1.rsplit('|'))   #Ҳ����ֱ������д������sep
print(s1.rsplit(sep='|',maxsplit=1))

#�ַ������жϲ���
#isidentifier(): �ж�ָ�����ַ����ǲ��ǺϷ��ı�ʶ��
#isspace(): �ж�ָ�����ַ����Ƿ�ȫ���ɿհ��ַ���ɣ��س������У�ˮƽ�Ʊ����
#isalpha(): �ж�ָ�����ַ����Ƿ�ȫ������ĸ���
#isdecimal(): �ж�ָ�����ַ����Ƿ�ȫ����ʮ���Ƶ��������
#isnumeric(): �ж�ָ�����ַ����Ƿ�ȫ�����������
#isalnum(): �ж�ָ�����ַ����Ƿ�ȫ������ĸ���������

s = 'hello,Python'
print('1.',s.isidentifier())                   #False
print('2.','hello'.isidentifier())             #True
print('3.','zhangsan'.isidentifier())          #True
print('4.','zhangsan_123'.isidentifier())      #True

print('5.','\t'.isspace())                     #True

print('6.','abc'.isalpha())                    #True
print('7.','kaixuan'.isalpha())                #True
print('8.','kaixuan1'.isalpha())               #False

print('9.','123'.isdecimal())                  #True
print('10.','123four'.isdecimal())             #False
print('11.','II II'.isdecimal())               #False

print('12.','123'.isnumeric())                 #True
print('13.','123four'.isnumeric())             #False
print('14.','II II'.isnumeric())               #False

print('15.','abc1'.isnumeric())                #False
print('16.','kaixuan123'.isnumeric())          #False
print('17.','abc!'.isnumeric())                #False
#���䣺��pycharm�У���������ĸ�����ı�ʾ���ֵ�һ�����ģ���������ּ�����ĸҲ������


#�ַ����滻��replace()����һ������ָ�����滻���ִ����ڶ�������ָ���滻�ִ����ַ������÷��������滻��õ����ַ�����
#                       �滻ǰ���ַ����������仯�����ø÷���ʱ����ͨ������������ָ������滻����
#�ַ����ϲ���join()�����б��Ԫ���е��ַ����ϲ���һ���ַ���

s = 'hello,Python'
print(s.replace('Python','Java'))
print(s,id(s))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python','C#',2))
print(s1,id(s1))

lst = ['hello','python','java']
print('|'.join(lst))
print(''.join(lst))
print(lst,id(lst))

t = ('hello','Python','C#')
print(''.join(t))
print(t,id(t))

print('*'.join('Python'))  #��python�ַ��������ַ�������