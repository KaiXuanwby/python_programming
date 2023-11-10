#列表元素的删除操作
#remove(): 一次删除一个元素;重复元素只删除第一个;元素不存在抛出ValueError
#pop(): 删除一个指定索引位置上的元素;指定索引不存在抛出IndexError;如果不指定索引，删除列表中最后一个元素
#切片: 一次至少删除一个元素
#clear(): 清空列表
#del: 删除列表

lst = [10,20,30,40,50,60,30]
lst.remove(30)
print(lst)

lst.pop(1)
print(lst)
lst.pop()
print(lst)

new_lst = lst[1:3]  #产生了新的列表对象,原列表没有变
print('before',lst)
print('after',new_lst)
print(id(lst),id(new_lst))

#不产生新的列表对象，而是删除列表中的内容
lst[1:3] = []
print(lst)
print(id(lst))

lst.clear
print(lst)

del lst
#print(lst) 报错



