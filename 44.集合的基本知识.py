#集合：python语言提供的内置数据结构
#      与列表字典一样都属于可变类型的序列
#      集合是没有value的字典
#也要通过hash()函数通过计算后确定位置

#集合的创建方式

#直接{}
s = {'Python','hello',90}
s1 = {1,2,2,3,3,4,4,4,9}  #集合中的元素不可以重复：类似字典中的键不可以重复
print(s)
print(s1)

#使用内置函数set()
s2 = set(range(6))
print(s2,type(s2))

s3 = set([1,2,5,5,5,6,6])
print(s3,type(s3))

print(set([3,4,53,56]))    #可以将列表元素转化为集合
print(set((3,4,43,435)))   #可以将元组转化为集合
print(set('Python'))       #可以将字符串转化为集合
print(set({124,3,4,4,5}))  #转不转都是集合类型
print(set())               #创建空集合

#定义一个空集合
s6 = {}    #dict字典类型
print(type(s6))
s7 = set()
print(type(s7))