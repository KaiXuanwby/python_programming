#元组是可迭代对象，所以可以使用for...in进行遍历

t = tuple(('python','hello',90))

print(t[0])
print(t[1])
print(t[2])
#print(t[3])   tuple index out of range

for item in t:
    print(item)




