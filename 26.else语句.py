#else语句：与else语句配合使用的三种情况---->if,while,for
#在循环时使用，当循环全部结束后才执行else

#输入密码
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