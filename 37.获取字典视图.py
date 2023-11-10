#获取字典视图的三个方法：
#keys(): 获取字典中所有的key
#values(): 获取字典中所有的value
#items(): 获取字典中所有的key,value对

scores = {'Bob':'23','kaixuan':'20','people':'11'}

keys = scores.keys()
print(keys,type(keys))
print(list(keys))      #将所有key所组成的视图转成列表

values = scores.values()
print(values,type(values))
print(list(values))

items = scores.items()
print(items,type(items))
print(list(items))     #元组(),转换之后的列表元素由元组组成


