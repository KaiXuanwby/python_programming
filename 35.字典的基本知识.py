#字典：python内置的数据结构之一，与列表一样是一个可变序列
#以 键值对 的方式存储数据，字典是一个 无序 的序列
#语法格式  字典名 = { ... , 键 : 值 , ...}  
#无序：字典中第一个放入的键值对并不一定就是第一个元素，而是要通过hash()函数通过计算后确定位置
#放在hash()函数中的的键必须是一个不可变序列
#字符串，字典，元组都是不可变序列
#字典的实现原理：字典的实现原理于查字典类似，查字典是先根据部首或拼音查找对应的页码，python中的字典是根据key查找value所在的位置
#字典的创建：使用花括号/使用内置函数dict()
#e.g: dict( name = 'jack',age = 20）

#使用花括号
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print(scores,type(scores))

#用内置函数dict()
student = dict( name = 'jack',age = 20)
print(student)

#空字典
d = {}
d1 = dict()
print(d)

#字典元素的获取
#[]   :scores['XXX']
#get():scores.get('XXX')
#二者的区别:[]如果字典中不存在指定的key，抛出keyError异常
#          :get()方法取值，如果字典中不存在指定的key，不会抛出keyError异常而是返回None，可以通过参数设置默认的value
#           以便指定的key不存在时返回

#[]
scores = {'Bob':'23','kaixuan':'20','people':'11'}
print(scores['kaixuan'])
#print(scores['Yeah'])  报错keyError

#get()
print(scores.get('kaixuan'))
print(scores.get('Yeah'))  #None
print(scores.get('boyu',520))  #520
