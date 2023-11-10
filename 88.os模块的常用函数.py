# os模块是python内置的与操作系统功能和文件系统相关的模块，该模块中的语句执行结果通常与操作系统有关，在不同的操作系统上运行
# 得到的结果可能不一样
# os模块与os.path模块用于对目录或文件进行操作
# os是与操作系统有关的一个模块

import os
os.system('notepad.exe')   # 和win+r结果相同
os.system('calc.exe')
# 直接调用可执行文件
os.startfile('路径')

#相关函数
# getcwd()                          返回当前的工作目录
# listdir(path)                     返回指定路径下的文件和目录信息
# mkdir(path[,mode])                创建目录
# makedirs(path1/path2....[,mode])  创建多级目录
# rmdir(path)                       删除目录
# removedirs(path1/path2......)     删除多级目录
# chdir(path)                       将path设置为当前工作目录

import os
print(os.getcwd())
lst = os.listdir('../chap15')    # 如果运行的模块程序包含在查找的目录下，直接写会报错，使用../返回上一级目录
print(lst)

os.mkdir('new-dir')
os.makedirs('A/B/C')               # 创建多级目录
os.rmdir('new-dir')
os.removedirs('A/B/C')
os.chdir('D:\\Python\\pychram\\chap14')
