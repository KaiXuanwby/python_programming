#input函数
#作用：接受来自用户的输入
#返回值类型：输入值的类型为str
#值的存储：使用=对输入的值进行存储
present=input('What do you want?')
print(present,type(present))

#从键盘录入两个整数，计算两个整数的和
n1 = input('Please enter a number(this number will be uesd to add)')
n2 = input('Please enter another number(this number will be uesd to add)')
print(n1+n2)#该表达式没有进行加法运算而是起连接作用，原因为输入值的类型为str，需要类型转换
print(type(n1),type(n2))
#解决方案
#法1
print(int(n1)+int(n2))
#法2
n1 = int(n1)
n2 = int(n2)
print(n1+n2)
#法3
a = int(input('Please enter a number(this number will be uesd to add)'))
b = int(input('Please enter another number(this number will be uesd to add)'))
print(a+b)