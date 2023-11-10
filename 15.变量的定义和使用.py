#变量：其值可以改变的量，实际上，变量是内存当中一个带标签的盒子
#变量名  赋值运算符   数据
# name       =        Bob
#e.g a = 10  则a中存储的是10所存在空间的id，即a指向含有10的空间

name = 'Juliet'
print(name)
#变量由三部分组成
#标识：表示对象所存储的内存地址，使用内置函数id(obj)来获取
#类型：表示对象的数据类型，使用内置函数type(obj)来获取
#值：表示对象所存储的具体数据，使用print(obj)可以将值快速打印输出
print('id',id(name))#标识
print('type',type(name))#类型
print('date',name)#值

#当多次赋值之后，变量名会指向新的空间
name = 'Juliet'
name = 'Romeo'#name内部所属的id变了，不是覆盖，而是新创建出一个空间
print(name)
print('id',id(name))#标识
print('type',type(name))#类型
print('date',name)#值
#原先的内部数据称为内存垃圾，将由垃圾处理器处理

#python中可以一行定义多个变量吗？若可以应使用什么格式的语句？
#是的，在Python中可以一行定义多个变量。你可以使用以下格式的语句来实现：
value1 = 1
value2 = 3
value3 = 8
var1,var2,var3 = value1,value2,value3
#或者使用一行的方式给多个变量赋相同的值：
var1 = var2 = var3 = value1
#在这些语句中，你可以将变量名和值用逗号分隔，将多个变量定义在一行上。这样就可以同时为多个变量赋值。