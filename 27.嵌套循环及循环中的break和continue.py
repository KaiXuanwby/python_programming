#嵌套循环：循环结构中又嵌套了另外的完整的循环结构，其中内层循环座位外层循环的循环体执行

#打印一个三行四列的矩形

for line in range(1,4):
    for column in range(1,5):
        print('*',end = '\t')  #end = ' ' 是print的一个参数，为末尾传递一个字符串，代替默认的换行符
    print()  #换行

#三角形
for line in range(1,10):
    for column in range(1,line+1):
        print('*',end = '\t')
    print()

#九九乘法表
for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print(num1,' * ',num2,'=',num1*num2,end='\t')
    print()

#二重循环中的break和continue：二重循环中的break和continue用于控制本层循环
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



