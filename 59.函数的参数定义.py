#函数定义默认值参数：函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参

def fun(a,b = 10):
    print(a,b)

#函数的调用
fun(100)  #只传递一个参数，b采用默认值
fun(20,30)  #30将默认值10替换

#def fun1(a =22 , b):     #SyntaxError: non-default argument follows default argument
#    print(a,b)
fun(55)

print()

#个数可变的位置参数
#定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
#使用*定义个数可变的位置形参，结果为一个元组
def fun(*args):   
    #仅可有一个个数可变的位置参数
    print(args)
fun(10)
fun(10,20,30)
#个数可变的关键字形参
#定义函数时，可能无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
#使用**定义个数可变的关键字形参，结果为一个字典
def fun1(**args):   
    #仅可有一个个数可变的关键字形参
    print(args)
fun1(a=10)
fun1(a=10,b=20,c=30)

def fun2(*args1,**args2):
    print(args1,args2)
    pass

#def fun3(**args1,*args2):  #报错：定义函数时，既有个数可变的位置参数，也有个数可变的关键字形参
 #   print(args1,args2)     #位置参数应放在关键字形参之前
 #  pass



def fun(a,b,c):          #a,b,c在函数的定义处，所以是形式参数
     print('a=',a) 
     print('b=',b)
     print('c=',c)

fun(10,20,30)            #函数调用时的参数传递，即位置传参
lst = [11,22,33]
fun(*lst)                #在函数调用期间，将列表中每个元素都转换为位置参数传入

fun(a=100,b=200,c=300)   #函数调用时的参数传递，即关键字传参
dic = {'a':100,'c':222,'b':333}
fun(**dic)               #在函数调用期间，将列表中每个元素都转换为关键字参数传入

def fun5(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun5(10,20,30,40)
fun5(a=10,b=20,c=30,d=40)
fun5(10,20,c=30,d=40)

#def fun(a,b,*,c,d   *号之后的参数在函数调用时，只能采用关键字传递)


#函数定义时形参的顺序问题
def fun7(a,b,c,*,d,**args):
    print(args)
    pass
def fun8(*args1,**args2):
    print(args1,args2)
    pass
def fun9(a,b=10,*args3,**args4):
    print(args3,args4)
    pass