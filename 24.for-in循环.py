#for-in循环用于遍历可迭代对象
#for-in循环：in表达从（字符串，序列等）中依次取值，又称为遍历
#for-in遍历的对象必须是可迭代对象，到目前为止，只有两个可迭代对象，一个是字符串，一个是序列
#语法结构：for 自定义的变量 in 可迭代对象
#              循环体
#循环体内不需要访问自定义变量，可以将自定义变量替代为下划线

for item in 'Python':     #第一次取出来的是P，将P赋值于item，将item的值输出
    print(item)
print(type(item))

#range()产生一个整数序列---->是一个可迭代对象
for things in range(0,20,2):
    print(things)
print(type(things))

#如果在循环体中不需要使用自定义变量，可以将自定义变量替代为下划线"_"
for _ in range(5):
    print('Yeah!')
 #当循环体未打印输出自定义变量时，序列元素的个数就变成了循环体循环的次数

 #使用for循环，计算1-100之间的偶数和
 

sum = 0
for num in range(0,101):
    if num%2==0:
         sum += num
    else:
         pass
print('sum is',sum)

#练习：要求输出100-999之间的水仙花数，水仙花数是一个三位数，各个数位上的数字的三次方之和等于原来的数
#e.g:153:3*3*3*+5*5*+1*1*1=153

for number in range(100,1000):
    num1 = number%10
    num2 = (number%100-num1)/10          #可改写为  num2 = number//10%10   在对10这样特殊数字取余%或取整//时，注意
    num3 = (number-num2*10-num1)/100     #可改写为  num3 = number//100
    if num1**3+num2**3+num3**3==number:
        print('One of the expected number is',number)


# //：如果整除数为10，就抹掉十位以后的所有数字，其他的数顺位继承，即为结果。如果整除数为100，就抹掉百位以后的所有数字，其他的数顺位继承，即为结果。
# %：如果取余数为10，就抹掉十位及以上的所有数字，余下的数为结果。如果取余数为100，就抹掉百位及以上的所有数字，余下的数为结果。
