#else��䣺��else������ʹ�õ��������---->if,while,for
#��ѭ��ʱʹ�ã���ѭ��ȫ���������ִ��else

#��������
for times in range(3):
    password = input('Plese enter your password: ')
    if(password=='123456'):
        print('Password correctly! ')
        break
    else:
        print('Password wrong! You just have ',2-times,' times to enter!')
else:
    print('You have uesd up the number of times, please contact the administrator for details.')



a = 0
while a<3:
    password = input('Plese enter your password')
    if(password=='123456'):
        print('Password correctly!')
        break
    else:
        print('Password wrong!You just have',3-a,'times to enter!')
    a += 1
else:
    print('You have uesd up the number of times, please contact the administrator for details.')