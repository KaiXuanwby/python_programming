#包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下
#代码规范
#避免模块名称冲突
#包与目录的区别：包含__init__.py文件的目录称为包
#目录里通常不包含__init__.py文件
#包的导入： import 包名.模块名
#包当中包含许多个模块

#导入
import package1.Module_A as ma             #package1.Module_A太长，可以通过 as 改名
#print(package1.Module_A.a)                #该式在没有写as时才可以正常运行
print(ma.a)

#导入带有包的模块时，注意：
#import package1
#import calc2
#使用import方式进行导入时，只能跟包名或者模块名

#from package1 import Module_A
#from package1.Module_A import a
#使用from...import可以导入包，模块，函数，变量

