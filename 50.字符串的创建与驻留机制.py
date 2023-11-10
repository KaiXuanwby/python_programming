#字符串：在python中的基本数据类型，是一个不可变的字符序列
#什么是驻留机制？
#仅保存一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，python的驻留机制对相同的字符串只保留一份拷贝，
#后续创建相同字符串时，不会开辟新空间，而是把该字符串的地址赋给新创建的变量

#字符串的定义
a = 'Python'
b = "Python"
c = '''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))     #id相同，说明内存空间中有且仅有一个python，只不过a,b,c三个变量指向这个内存空间
print(a == b)

#驻留机制的几种情况（交互模式）
#字符串长度为0或1时
s1=''
s2=''
print(s1 is s2)

s1='%'
s2='%'
print(s1 is s2)

#符合标识符的字符串
s1='abc%'
s2='abc%'                      #%不符合标识符
print(s1 is s2,s1 == s2)       #在交互式下s1 is s2的结果为False
print(id(s1),id(s2))           #内存地址不同，但存放的数据地址是相同的

#字符串只在编译时进行驻留，而非运行时
a = 'abc'
b = 'ab'+'c'
c = ''.join(['ab','c'])
print(a is b)   #True
print(a is c)   #False   b的值是在运行之前就已经连接好了，c的值是在运行的过程中通过join方法对数据进行连接的
print(c)
print(type(c),a,type(a))

#[-5,256]之间的整数数字
a = -5
b = -5
print(a is b)   #True

a = -6
b = -6
print(a is b)   #在交互式下为False

#sys中的intern方法强制2个字符串指向同一个对象
import sys
s1='abc%'
s2='abc%'                     
print(a is b)     #False
a = sys.intern(b)
print(a is b)     #True

#pycharm对字符串进行了优化处理:即使用编译器所得结果不一样
#字符串驻留机制优缺点
#优：需要相同字符串时，可以直接从字符池里拿来使用，避免频繁的创建销毁，提升效率节约内存，
#    因此拼接字符串和修改字符串是比较影响性能的
#在需要字符串拼接时建议使用 str类型的join 方法，而非+，因为join()方法是先计算出所有字符串中的长度，然后再拷贝，
#    只new一次对象，效率比+高



