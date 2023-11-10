#集合的相关操作

#集合元素的判断操作：in  /   not in
s = {10,20,30,40,50}
print(10 in s)         #True
print(100 in s)        #False
print(10 not in s)     #False
print(100 not in s)    #True


#集合元素的新增操作：调用add()方法，一次添加一个元素
#                    调用update()方法至少添加一个元素
s.add(80)
print(s)
s.update({200,400,300})
print(s)
s.update([100,99,8])
print(s)
s.update((78,64,56))
print(s)

#集合元素的删除操作：调用remove()，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
#                    调用discard(),一次删除一个指定元素，如果指定的元素不存在不抛出异常
#                    调用pop(),一次只删除一个任意元素
#                    调用clear()方法，清空集合
s.remove(100)
print(s)
#s.remove(500)       #KeyError:500
#print(s)
s.discard(500)       #不报错
print(s)
s.pop()              #删除的总是集合的第一个元素（hash排序后）
print(s)
#s.pop(400)          #pop不可以添加参数，只能写无参数的，写入参数会报错
s.clear()
print(s)
