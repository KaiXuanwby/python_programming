#列表：变量可以储存一个元素，而列表是一个“大容器”可以储存N多个元素，程序可以方便的对这些数据进行整体操作
#列表相当于其他语言中的数组

a = 10  #变量存储的是一个对象的引用
lst = ['hello','world',98]  #首先，lst为一个变量，其类型为数组，可以将该变量看作一个指针，指向一个指针集合
print(id(lst))
print(id(lst[0]),id(lst[1]),id(lst[2]))#在指针集合中，元素个数为列表中的元素个数，这些元素可以看作变量，分别指向对应的内存空间
print(type(lst))             #二级指针
print(lst)

#列表的创建：列表需要使用中括号[]，元素之间用英文的逗号进行分隔
#创建方式：使用中括号，调用内置函数list()

lst1 = ['kaixuan','my dear',7]
lst2 = list(['kaixuan','my dear',7])


#空列表
lst = []
lst1 = list()
#列表的特点：列表元素按顺序有序排列
#            索引映射唯一一个数据
print(lst2[0],lst2[-3],lst[2],lst[-1]) #索引
#            列表可以存储重复数据
#            任意数据类型混存
#            根据需要动态分配和回收内存

#列表的查询操作：获取列表中指定元素的索引
#index():如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
#如果查询元素在列表中不存在，则会抛出ValueError
#还可以在指定的start和stop中查找

lst3 = ['juanwang',666,'geng','wang','jiang'] 
print(lst3.index('geng'))
#print(lst3.index('juanwang',1,3))  报错
print(lst3.index('juanwang',0,4))

#                获取列表中的单个元素
#正向索引从0到N-1（从右向左）   e.g: lst[0]
#逆向索引从-N到-1   e.g: lst[-N]
#指定索引不存在，抛出indexError
lst4 = ['python','workhard',98,'hello','world',556]
print(lst4[2])
print(lst4[-3])
print(lst4[10])
