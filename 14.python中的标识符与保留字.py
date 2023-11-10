# coding=gbk

# 规矩
# 保留字：有一些单词被赋予了特殊的含义，这些单词你在给你的任何对象起名字时都不能用
# import  keyword  print(keyword.kwlist)
# python中一切皆对象。e.g 在新建python项目时，XXXXX.py,该文件名不可以用保留字

import keyword
print(keyword.kwlist)
# 通过这两行代码，执行后可以找到保留字

# 标识符：变量，函数，类，模块和其他对象的起的名字就叫标识符
# 规则：
# 可以使用字母，数字，下划线
# 不能以数字开头
# 不能是保留字
# 严格区分大小写
