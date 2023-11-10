#循环结构：反复做同一件事的情况，称为循环
#循环的分类：while循环     for-in循环

#while循环多用于次数不固定的循环，初始条件不成立，一次都不执行
#语法结构： while 条件表达式:
#               条件执行体（循环体）
#选择结构与循环结构的区别
#if判断一次，条件为true执行一次
#while是判断N+1次，条件为True执行N次

a = 1
while a<10:
    print(a)
    a+=1
#四步循环法：初始化变量，条件判断，条件执行体（循环体），改变变量

a = 0
sum = 0
while a < 5:
    sum+=a
    a+=1
print('sum is',sum)

#练习：计算1-100之间的偶数和
sum_a = 0
a = 1
while a<=100:
    if a%2==0: #可以改为if a%2==0  或 if not bool(a%2)
        sum_a += a
    else:
        pass
    a += 1
print('sum is',sum_a)

