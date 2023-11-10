#流程控制语句break：用于结束循环结构，通常与分支结构if一起使用

#从键盘录入密码，最多录入三次，如果正确则结束循环
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



#流程控制语句continue:用于结束当前循环，进入下一次循环，通常与分支结构if一起使用

#要求输出1-50之间所有5的倍数

for number in range(1,51):
    if number%5==0:
        print(number,'is a multiple of 5')

for number in range(1,51):
    if number%5 != 0:
       continue  #也可以写pass，因为if条件已经成立，else不执行，无所谓有没有continue
    else:
        print(number,'is a multiple of 5')