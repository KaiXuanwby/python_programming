#变量的作用域
#程序代码能访问该变量的区域
#根据变量有效范围可分为
#局部变量：在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
#全局变量：函数体外定义的变量，可作用于函数内外

def fun(a,b):
    c=a+b           #c为局部变量
    print(c)

name = 'kaixuan'    #name为全局变量
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age     #global声明:局部变量就会变成全局变量
    age = 20
    print(age)
fun3()
print(age)
