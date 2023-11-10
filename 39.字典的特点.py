#字典中的所有元素都是一个key-value对，key不允许重复，value可以重复
#字典中的元素是无序的
#字典中的key必须是不可变对象
#字典也可以根据需要动态的伸缩
#字典会浪费较大的内存，是一种使用空间换时间的数据结构

d = {'name':'kaixuan','name':'wang'}   #key不允许重复
print(d)

d = {'name':'kaixuan','nickname':'kaixuan'}    #value可以重复
print(d)

lst = [10,20,30]
lst.insert(1,100)
print(lst)
#d = {lst:100}   报错
#print(d)