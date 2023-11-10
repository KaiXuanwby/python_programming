#编码：将字符串转化为二进制数据（bytes）
#解码：将bytes类型的数据转换成字符串类型

s = 'today'
print(s.encode(encoding = 'GBK'))  #GBK编码格式中一个中文占两个字节
print(s.encode(encoding = 'UTF-8'))  #UTF-8编码格式中一个中文占三个字节
#不同的编码格式决定占用字节数

#byte代表的就是一个二进制数据（字节类型的数据）
byte = s.encode(encoding = 'GBK')
print(byte.decode(encoding = 'GBK'))

byte = s.encode(encoding = 'UTF-8')
print(byte.decode(encoding = 'UTF-8'))
#编码和解码的格式一定要相同


