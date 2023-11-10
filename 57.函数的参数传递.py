#函数调用的参数传递
#位置实参：根据形参对应的位置进行实参传递
#关键字实参：根据形参名称进行实参传递

def calc(a,b):      #调用时数据占了a,b的位置，a,b为形式参数，形参的位置在函数的定义处
    c = a+b
    return c

result = calc(10,20)  #10，20称为实际参数的值，实参的位置是函数的调用处
print(result)

result2 = calc(b = 10,a = 20)   #左侧的变量名称为关键字实际参数
print(result2)

def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)

n1 = 11
n2 = [10,20,30]
print('n1=',n1)
print('n2=',n2)
fun(n1,n2)            #位置传参
print('n1=',n1)
print('n2=',n2)
#在函数的调用过程中，进行参数的传递
#如果是不可变对象，在函数体的修改不会影响实参的值 arg1的修改为100，不会影响n1的值
#如果是可变对象，在函数体的修改会影响到实参的值   arg2的修改.append(10)，会影响n2的值