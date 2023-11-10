#Debug:清除bug
#SyntaxError：粗心导致的语法错误

age = input('Please enter your age:')    
print(type(age))
#if age >= 18:
if int(age) >= 18:
    print('you are adult')

i = 0
while i<10:
        print(i)
        i +=1

#常见类型
#漏掉末尾的冒号，如if语句，循环语句,else语句
#缩进错误
#把英文符号写成中文符号
#字符串拼接的时候，把字符串和数字拼到一起
#没有定义变量，比如说while循环的变量
#‘==’和‘=’运算符混用


#知识点不熟练导致的错误
#IndexError:索引越界问题
lst = [11,22,33,44]
#print(lst[4])       #IndexError
print(lst[3])
#append()方法掌握不熟练
lst = []
#lst = append('A','B','C')  append方法一次只能添加一个元素
lst.append('A')     
print(lst)

#思路不清导致的问题解决方案
#使用print()函数
#使用#暂时注释掉部分代码

#被动掉坑所导致的异常：程序代码逻辑没有错，只是因为用户错误操作或者一些例外情况而导致的程序崩溃
#解决方案异常处理机制，在异常出现时即使捕获
#    try:
#       可能会出现异常的代码
#    except 异常类型:
#       异常处理代码（报错后执行的代码）

try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
    print('result is ',result)
except ZeroDivisionError :
    print('Sorry, zero is unacceptable')
print('over')

#多个except结构：捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
#    try:
#       可能会出现异常的代码
#    except 异常类型1:
#       异常处理代码（报错后执行的代码）
#    except 异常类型2:
#       异常处理代码（报错后执行的代码）
#    ......
#    except BaseException:
#       异常处理代码（报错后执行的代码）

try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
    print('result is ',result)
except ZeroDivisionError :
    print('Sorry, zero is unacceptable')
    print('over')
except ValueError :
    print('cannot change str to number')
except BaseException as e:
    print(e)


#try...except...else结构
#如果try块中没有抛出异常，则执行else块，如果try中抛出异常，则执行except块
try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
except BaseException as e:             #把错误叫做e,如果出错，则输出出错原因
    print('Wrong!')
    print(e)
else:    
    print('result is ',result)


#try...except...else...finally结构
#finally块是无论是否发生异常均会被执行的代码，能常用来释放try块中申请的资源
try:
    a = int(input('Please enter the first number:'))
    b = int(input('Please enter the second number:'))
    result = a/b
except BaseException as e:             #把错误叫做e,如果出错，则输出出错原因
    print('Wrong!')
    print(e)
else:    
    print('result is ',result)
finally:
    print('Programm is over, thanks')