#列表生成式简称“生成列表的公式”
#语法格式： [表示列表元素的表达式 for 自定义变量 in 可迭代对象]
#注意事项：“表示列表元素的表达式”中通常包含自定义变量

lst = [i for i in range(1,10)]
print(lst)
lst = [i*i for i in range(1,10)]
print(lst)
lst = [i*2 for i in range(1,11)]
print(lst)
lst = [i*2 for i in range(1,6)]
print(lst)

#当然，基本创建也可以
lst2 = list(range(1,11))
print(lst2)

