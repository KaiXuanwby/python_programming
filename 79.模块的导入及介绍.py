#模块的英文为Modules
#函数与模块的关系：一个模块可以包含n多个函数
#在Python中一个扩展名为.py的文件就是一个模块
#使用模块的好处：方便其他程序和脚本的导入并使用
#                避免函数名与变量名冲突
#                提高代码的可维护性
#                提高代码的可重用性
#模块中包含函数，类，语句

#导入模块
#import 模块名称 [as 别名]
#from 模块名称 import 函数/变量/类
import math              #关于数学运算
print(id(math))
print(type(math))
print(math)
print(math.pi)
print('-------------------------------')
print(dir(math))                            #观察math模块中有哪些内容
print(math.pow(2,3),type(math.pow(2,3)))    #pow(a,b)a的b次幂
print(math.ceil(9.001))                     #ceil向上取整
print(math.floor(9.9999))                   #向下取整

#若只想使用math当中的pi，可以这样写
from math import pi
print(pi)
print(pow(2,3))                              #常规使用（buitins模块）返回值为int
print(math.pow(2,3))                         #math引用(math模块) 返回值为float

from math import pow
print(pow(2,3))

#自定义模块的导入
import calculation
print(calculation.add(10,20))
print(calculation.div(10,20))

from calculation import add
print(add(10,20))