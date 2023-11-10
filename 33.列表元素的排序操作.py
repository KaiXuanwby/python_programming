#列表元素的排序操作：
#调用sort()方法：列表中的所有元素默认按从小到大的顺序进行排列，可以指定reverse = True,进行降序排序，不产生新的列表对象，原列表变

lst = [20,40,10,98,54]
print('before',lst,id(lst))
lst.sort()
print('after',lst,id(lst))  #id相同，说明是在原列表的基础上进行排序

#降序
lst.sort(reverse = True)   #reserve = False为升序排序
print(lst,id(lst))


#调用内置函数sorted()，可以指定reverse = True,进行降序排序原列表不发生改变,产生新的列表对象，原列表不变
lst = [20,40,10,98,54]
print('before',lst,id(lst))
new_lst = sorted(lst)   #sorted把原列表的元素排好序，然后放到一个新列表里
print(new_lst,id(new_lst))
desc_lst = sorted(lst,reverse = True)
print(desc_lst,id(desc_lst))
