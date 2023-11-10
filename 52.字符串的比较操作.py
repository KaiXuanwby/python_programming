#字符串的比较操作
#运算符：> , >= , < , <= , == , !=
#比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，
#          直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有字符将不再被比较
#比较原理：两上字符进行比较难时，比较的是其ordinal value（原始值），调用内置函数ord，可以得到指定字符的ordinal value
#与内置函数ord对应的是chr，调用内置函数chr时指定ordinal value可以得到其对应的字符

print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b'))
print(ord('k'))

print(chr(97),chr(98))
print(chr(26472))

#==与is的区别
#==比较的是 value
#is比较的是id

a = b = 'Python'
c = 'Python'
print(a == b)   #True
print(b == c)   #True
print(a is b)   #True
print(a is c)   #True
print(id(a))
print(id(b))
print(id(c))  #字符串的驻留机制
