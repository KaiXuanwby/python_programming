#集合的数学操作：交集，并集，差集，对称差集


#交集操作: intersection()与&等价，均属于交集操作
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)    
print(s1)
print(s2)


#并集操作: union()与|等价
print(s1.union(s2))
print(s1 | s2)
print(s1)
print(s2)

#差集操作：difference()与-等价
print(s1.difference(s2))   #s1减去s2集合后剩下的元素
print(s1-s2)
print(s1)
print(s2)

#对称差集:symmetric_difference与^等价--->A,B集合的并集减去交集
print(s1.symmetric_difference(s2))
print(s1^ s2)
print(s1)
print(s2)
