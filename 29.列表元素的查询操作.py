#列表元素的查询操作
#获取列表中的多个元素
#语法格式：列表名[ start : stop : step]
#切片的结果：原列表片段的拷贝

#切片的范围：[start:stop]

#step默认为1 ，简写为[start:stop]

#step为正数-->[:stop:step]-->切片的第一个元素默认是列表的第一个元素-->从start开始往后计算切片
#         |-->[start::step]-->切片的最后一个元素默认是列表的最后一个元素-->从start开始往后计算切片

#step为负数-->[:stop:step]-->切片的第一个元素默认是列表的最后一个元素-->从start开始往前计算切片
#         |-->[start::step]-->切片的最后一个元素默认是列表的第一个元素-->从start开始往前计算切片

lst = [10,20,30,40,50,60,70,80]
#print(lst[1:6:1])  #新的列表对象
print('before',id(lst))
lst2 = lst[1:6:1]
print('after',id(lst2))
print(lst[1:6])   #step默认为1
print(lst[1:6:])
print(lst[1:6:2])
print(lst[:6:2])
print(lst[1::2])

print(lst[::-1])    #逆序输出元素
print(lst[7::-1])
print(lst[6:0:-2])


#判断指定元素在列表中是否存在
#元素 in 列表名
#元素 not in 列表名
#列表元素的遍历
#for 迭代变量 in 列表名

print('p' in 'python')  #True
print('k' not in 'python')  #True

lst = [10,20,'python','hello']
print(10 in lst)   #True
print(100 in lst)   #False
print(10 not in lst)   #False
print(100 not in lst)   #True
#遍历输出列表元素
for item in lst:
    print(item)