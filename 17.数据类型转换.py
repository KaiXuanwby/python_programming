#数据类型转换：为什么需要数据类型转换？
#将不同数据类型的数据拼接在一起
name = 'a'
age = 20

print(type(name),type(age))#数据类型不相同
print('My name is ',name,'I\'m ',age,' years old')
#print('My name is '+name+'I\'m '+age+' years old')#执行后报错：can only concatenate str (not "int") to str
#（不可以将字符串str和int类型用加号进行连接）
#‘+’ 称为连接符
#解决方案：类型转换
print('My name is '+name+'I\'m '+str(age)+' years old')#将int类型通过str()转换成了str类型

#str()   int()   float()


#str()：将其他类型转化为str,也可以用引号转换   e.g：‘123’

a = 10
b = 198.5
c = False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))#转换时相当于形参变量（复制），只改变当下不改变本身
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

#int()：将其他类型转化为int

s1  = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))#将str转成int类型，字符串变为数字串
print(int(f1),type(int(f1)))#将float转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2))) 报错：将str转成int类型，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3)))  报错：将str转成int类型时，字符串必须为数字串（整数），非数字串不允许转换

#float()：将其他类型转化为float
s1  = '128.98'
s2 = '76'
ff = True
s3 = 'hello'
i = 98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))   报错：字符串中的数据如果是非字符串，则不允许转换
print(float(i),type(float(i)))