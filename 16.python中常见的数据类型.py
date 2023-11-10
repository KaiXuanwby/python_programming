#常用的数据类型
#整数类型：int    e.g 98
#浮点数类型：float    e.g 98.88
#布尔类型：bool    e.g  True or False(只有这两个值)
#字符串类型：str    e.g  you are juanwang 

#整数类型：int（integer） 可以表示正数，负数和零
#整数的不同进制表示方式
#十进制  默认进制  0-9
#二进制  以0b开头  0-1
#八进制  以0o开头  0-7
#十六进制  以0x开头  0-F
n1 = 90
n2 = -76
n3 = 0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

print('10:',118)
print('2:',0b10101111)#二进制  以0b开头
print('8:',0o176)#八进制  以0o开头
print('16:',0x1EAF)


#浮点数类型：float
#浮点数由整数部分和小数部分组成
#浮点数存储不精确
a = 3.14159
print(a,type(a))
n1 = 1.1
n2 = 2.2
print(n1+n2)
print(1.1+2.2)#使用浮点数进行计算时，可能会出现小数位不确定的情况
print(1.1+2.1)#不是所有浮点数相加都会出现不精确的情况
#解决方案：导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型：bool(boolean)
#用来表示真或假的值      True表示真  False表示假
#布尔值可以转化为整数    True-->1    False-->0
f1 = True
f2 = False
print(f1,type(f1))
print(f2,type(f2))
#布尔值可以转化成整数进行计算，使用时直接当成整数进行加减
print(f1+1)  #2（1+1）
print(f2+1)  #1（0+1）

#字符串类型：str
#字符串又被称为不可变的字符序列
#可以使用 '单引号' "双引号" ''' 三引号'''或"""三引号"""来定义
#单引号和双引号定义的字符串必须在一行
#三引号定义的字符串可以分布在连续的多行
str1 = 'Juliet and Romeo'
print(str1,type(str1))
str2 = "Juliet and Romeo"
print(str2,type(str2))
str3 = '''Juliet an
d Romeo'''
print(str3,type(str3))
str4 = """Juliet 
and Romeo"""
print(str4,type(str4))