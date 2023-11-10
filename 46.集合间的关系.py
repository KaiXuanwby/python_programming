#两个集合是否相等：可以使用运算符 == 或 ！= 进行判断
#一个集合是否是另一个集合的子集：可以调用方法issubset进行判断
#一个集合是否是另一个集合的超集：可以调用方法issuperset进行判断
#两个集合是否没有交集：可以调用方法isdisjoint进行判断


#两个集合是否相等，元素相等就相等
s = {10,20,30,40}
s2 = {30,40,20,10}
print(s == s2)      #True
print(s != s2)      #False


s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.issubset(s1))  #s2是s1的子集吗  True
print(s3.issubset(s1))  #s3是s1的子集吗  False

print(s1.issuperset(s2))   #s1是s2的超集吗  True
print(s1.issuperset(s3))   #s1是s3的超集吗  False


print(s2.isdisjoint(s3))    #False   有交集为False
s4 = {100,200,300}
print(s2.isdisjoint(s4))    #True    没有交集为True