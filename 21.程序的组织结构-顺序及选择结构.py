#任何简单或复杂的算法都可以由顺序结构、选择结构和循环结构这三种基本结构组合而成
#顺序结构
#选择结构：if语句
#循环结构: while语句     for-in语句


#顺序结构：程序从上到下执行代码，中间没有任何判断和跳转，直到程序结束
print('---------- start ----------')
print('open the door')
print('put the things to it')
print('close the door')
print('---------- end ----------')#通过添加断点来清晰观察

#对象的布尔值
#python 中一切皆对象，所有对象都有一个布尔值
#获取对象的布尔值：使用内置函数bool()
#这些对象的布尔值为False：False 数值0，None,空字符串，空列表，空元组，空字典，空集合
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
#除上述对象以外，其余对象的布尔值均为True


#选择结构：根据判断条件的布尔值选择性的执行部分代码。明确的让计算机知道在什么条件下，该去做什么
#单分支结构：中文语义：如果...就...
#"""语法结构：if+条件表达式+:
#                 条件执行体
#"""
#在条件表达式处如果不写表达式，而是直接输入一个值或者变量，对于真假的判断将按照输入的值或者变量的布尔值进行判断
money = 1000
s = float(input('How much money would you want to take?'))
if money>=s:
    money-=s
    print('It has been token successfully!\n you still have',money,'money')

#双分支结构：中文语义：如果...就...不满足...就...
#语法结构：if+条件表达式+:
#             条件执行体1
#          else+:
#             条件执行体2
num = int(input('Please enter an integer number:'))

if num%2==0:
    print('num is an even number.\t',num)
else:
    print('num is an uneven/odd number.\t',num)


#多分支结构
#语法结构：if+条件表达式1+:
#             条件执行体1
#          elif+条件表达式2+:
#             条件执行体2
#          elif+条件表达式3+:
#             条件执行体3
#            ..............
#          [else:]         ----->  可写可不写
#             条件执行体N

grade = int(input('please enter your grade'))
if   grade<=100 and grade>=90:             #此处可改写为90<=grade<=100
    print('You has got the A standard.')
elif grade<90 and grade>=80:               #此处可改写为80<=grade<=89
    print('You has got the B standard.')
elif grade<80 and grade>=70:               #此处可改写为70<=grade<=79
    print('You has got the C standard.')
elif grade<70 and grade>=60:               #此处可改写为60<=grade<=69
    print('You has got the D standard.')
elif grade<60 and grade>0:                 #此处可改写为0<=grade<=59
    print('You has got the E standard.')
else:
    print('Your grade is illegal,try again.')


#嵌套if
#语法结构：if+条件表达式1:
#              if+内层条件表达式：
#                  内层条件执行体1
#              else:
#                  内层条件执行体2
#          else:
#              条件执行体

membership = int(input('Are you a member of our store?\nIf you are,please enter 1.\nIf you aren\'t,please eneter 0'))
consumption  = float(input('How much things did you cost? '))
if membership==1:
    if consumption>=200:
        consumption *= 0.8
    elif 100<=consumption<200:
        consumption *= 0.9
    else:
        consumption=consumption
elif membership==0:
    if consumption>=200:
        consumption *= 0.95
    else:
        consumption = consumption

print('Your consumption is',consumption)

#条件表达式：if...else的简写
#语法结构：   x  if  判断条件  else  y
#运算规则;如果判断条件的布尔值为True,条件表达式的返回值为x，否则条件表达式的返回值为False

num1 = int(input('Please enter the first number:'))
num2 = int(input('Please enter the second number:'))

#"""
if num1 >= num2:
    print(num1,'>=',num2)
else:
    print(num1,'<',num2)
#"""

print(   str(num1)+'>='+str(num2)   if num1 >= num2 else   str(num1)+'<'+str(num2)   )

#pass语句
#pass语句什么都不做，只是一个占位符，用在语法上需要语句的地方
#什么时候使用：先搭建语法结构，还没想好代码怎么写的时候
#哪些语句一起使用：if语句的条件执行体
#                  for-in语句的循环体
#                  定义函数的函数体