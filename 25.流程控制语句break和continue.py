#���̿������break�����ڽ���ѭ���ṹ��ͨ�����֧�ṹifһ��ʹ��

#�Ӽ���¼�����룬���¼�����Σ������ȷ�����ѭ��
for times in range(3):
    password = input('Plese enter your password')
    if(password=='123456'):
        print('Password correctly!')
        break
    else:
        print('Password wrong!You just have',3-times,'times to enter!')

a = 0
while a<3:
    password = input('Plese enter your password')
    if(password=='123456'):
        print('Password correctly!')
        break
    else:
        print('Password wrong!You just have',3-a,'times to enter!')
    a += 1



#���̿������continue:���ڽ�����ǰѭ����������һ��ѭ����ͨ�����֧�ṹifһ��ʹ��

#Ҫ�����1-50֮������5�ı���

for number in range(1,51):
    if number%5==0:
        print(number,'is a multiple of 5')

for number in range(1,51):
    if number%5 != 0:
       continue  #Ҳ����дpass����Ϊif�����Ѿ�������else��ִ�У�����ν��û��continue
    else:
        print(number,'is a multiple of 5')