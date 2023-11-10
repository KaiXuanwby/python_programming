#列表元素的增加操作
#append()：在列表的末尾添加一个元素
#extend()：在列表的末尾至少添加一个元素
#insert()：在列表的任意位置添加一个元素
#切片：在列表的任意位置至少添加一个元素

lst = [10,20,30]
print('before',lst,id(lst))
lst.append(100)
print('after',lst,id(lst))
lst2 = ['hello','world']
lst.append(lst2)   #将lst2作为一个元素添加到列表的末尾
print(lst)
lst.extend(lst2)
#向列表的末尾一次性添加多个元素
print(lst)

lst.insert(1,90)  #把90这个元素添加到索引为1的地方去
print(lst)

lst3 = [True,False,'hello']
#lst[1:] = lst3
lst[1:1] = lst3
print(lst)


