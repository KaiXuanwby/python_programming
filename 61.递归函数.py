#什么是递归函数：如果在一个函数的函数体内调用了该函数本身，这个函数就称为递归函数
#递归的组成部分：递归调用与递归终止条件
#递归的调用过程：每递归调用一次函数，都会在栈内存分配一个栈帧
#                每执行完一次函数，都会释放相应的空间
#递归的优缺点：缺：占用内存多，效率低下
#              优：思路和代码简单

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))

#斐波那契数列:第一，二项为1，某一项为前两项之和
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#第六位的数字
print(fib(6))

#输出这个数列前六位上的数字
for i in range(1,7):
    print(fib(i))

