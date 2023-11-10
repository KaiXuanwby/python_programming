#内置函数range()：用于生成一个整数序列  内置函数:不需要加任何前置，可以直接使用的函数
#创建rang对象的三种方式：
#range(stop)----->创建一个（0，stop）之间的整数序列，步长为1
#range(start,stop)----->创建一个（start，stop）之间的整数序列，步长为1
#range(start,stop,step----->创建一个（start，stop）之间的整数序列，步长为step
#返回值是一个迭代器对象
#rabge类型的优点：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，
#因为仅仅需要存储start,stop和step，只有当用到range对象时，才会去计算序列中的相关元素
#in与not in判断序列中是否存在（不存在)指定的整数

""" -------------first -------------"""
r = range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],默认从0开始，默认相差为1，称为步长
print(r)
print(list(r))#用于查看range对象中的整数序列  ---->list表示列表

""" -------------second -------------"""
r = range(1,10)   #[1, 2, 3, 4, 5, 6, 7, 8, 9] 取值区间左闭右开（含头不含尾）
print(r)
print(list(r))

""" -------------third -------------"""
r = range(1,15,2)   #[1, 3, 5, 7, 9, 11, 13]
print(r)
print(list(r))

""" -------------whether the number exist -------------"""
print(10 in r)  #False,10不在当前r的整数序列中
print(9 in r)   #True
print(10 not in r)   #True
print(9 not in r)   #False

print(range(1,20,1))  #[1.......19]
print(range(1,101,1))  #[1.......100]
#20和101所占据的空间大小是相同的，只有当真正使用这些数据时，占用的内存才会出现差距