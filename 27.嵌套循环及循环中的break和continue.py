#Ƕ��ѭ����ѭ���ṹ����Ƕ���������������ѭ���ṹ�������ڲ�ѭ����λ���ѭ����ѭ����ִ��

#��ӡһ���������еľ���

for line in range(1,4):
    for column in range(1,5):
        print('*',end = '\t')  #end = ' ' ��print��һ��������Ϊĩβ����һ���ַ���������Ĭ�ϵĻ��з�
    print()  #����

#������
for line in range(1,10):
    for column in range(1,line+1):
        print('*',end = '\t')
    print()

#�žų˷���
for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print(num1,' * ',num2,'=',num1*num2,end='\t')
    print()

#����ѭ���е�break��continue������ѭ���е�break��continue���ڿ��Ʊ���ѭ��
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end = '\t')
    print()



