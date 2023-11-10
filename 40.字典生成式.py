#字典生成式:{ 表示字典key的表达式 : 表示字典value的表达式 for 自定义表示key的变量,自定义表示value的变量 in 可迭代对象 }
#内置函数zip()
#用于将可迭代对象作为参数，将对象中对应元素打包成一个元组，然后返回由这些元组组成的列表


items = ['Firuts','Books','Others']
prices = ['96','78','85']       #若值多于键，则只取前三

d = {item.upper():price for item , price in zip(items,prices)}  #upper将items中的对象全部转化为大写
print(d)




