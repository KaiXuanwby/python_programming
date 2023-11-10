#元组：python内置的数据结构之一，是一个不可变序列
#不变序列：字符串，元组
#  不变序列：没有增、删、改的操作
#可变序列：列表、字典
#  可变序列：可以对序列执行增、删、改操作，对象地址不发生更改

lst = [10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

s = 'hello'
print(id(s))
s = s + 'world'
print(id(s))
print(s)

#元组： ( 元素对象 , 元素对象 , ...)
#元组的创建方式：
#直接小括号：  t = ('python','hello',90)
#内置函数tuple:   t = tuple(('python','hello',90))
#只包含一个元素的元组需要使用逗号和小括号:   t = (10,)

t = ('python','hello',90)
print(t,type(t))

t1 = 'python','hello',90
print(t1,type(t1))

t2 = ('python',)   #如果元组中只有一个元素，逗号不能省
print(t2,type(t2))

t3 = tuple(('python','hello',90))
print(t3,type(t3))

#空元组的创建方式
t4 = ()
t5 = tuple()