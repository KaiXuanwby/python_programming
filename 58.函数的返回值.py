#函数返回多个值时，结果为元组

print(bool(0))
print(bool(1))

def fun(num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,34,23,44,53,55]))
#（1）函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】  return可以省略不写
#（2）函数的返回值，如果是1个，直接返回类型
#（3）函数的返回值，如果是多个，返回的结果为元组

def fun1():
    print('hello')
fun1()

def fun2():
    return 'hello'
print(fun2())

def fun3():
    return 'hello','world'
print(fun3())

#函数在定义时，是否需要返回值，视情况而定