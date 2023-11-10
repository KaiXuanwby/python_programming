#格式化字符串：按一定格式输出的字符串
#使用%作为占位符： 字符串%s  整数%i或%d  浮点数%f
#使用{}作为占位符,format方法

name = 'kaixuan'
age = 19
print('My name is %s , %d years this year' % (name,age))
print('My name is {0} , {1} years this year'.format(name,age))
print(f'My name is {name} , {age} years this year')

print('%10d' % 99)          #10表示的是宽度
print('%.3f' % 3.14159)     #.3表示的是小数点后三位
print('%10.3f' % 3.14159)   #10.3总宽度为10，小数点后三位

print('{0:.3}'.format(3.14159))   #.3表示三位数
print('{:.3f}'.format(3.14159))   #.3表示三位小数，0可以省略
print('{:10.3f}'.format(3.14159))   #.3表示三位小数，0可以省略
