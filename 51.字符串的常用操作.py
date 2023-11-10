#字符串的查询操作
#index():查找子串substr第一次出现的位置，如果查找的子串不存在，则抛出ValueError
#rindex():查找子串substr最后一次出现的位置，如果查找的子串不存在，则抛出ValueError
#find():查找子串substr第一次出现的位置，如果查找的子串不存在，则返回-1
#rfind():查找子串substr最后一次出现的位置，如果查找的子串不存在，则返回-1
#字符串是有序的，有索引
s = 'hello,hello'
print(s.index('lo'))     #3
print(s.find('lo'))      #3
print(s.rindex('lo'))    #9     
print(s.rfind('lo'))     #9

'''
     <-----------------------------
    -11-10-9 -8 -7 -6 -5 -4 -3 -2- 1
     h  e  l  l  o  ,  h  e  l  l  o
     0  1  2  3  4  5  6  7  8  9 10
     -------------------------------->
'''

#print(s.index('k'))     #ValueError:substring not found
print(s.find('k'))      #-1
#print(s.rindex('k'))    #ValueError:substring not found 
print(s.rfind('k'))     #-1



#字符串的大小写转换方式
#upper():把字符串中所有字符转换为大写字母
#lower():把字符串中所有字符转换为小写字母
#swapcase():把字符串中所有大写字符转换为小写字母，把字符串中所有小写字符转换为大写字母
#capitalize():把第一个字符转换为大写，其余转换为小写
#title():把每个单词第一个字符转换为大写，每个单词的剩余字符转换为小写

s = 'hello,python'
a = s.upper()
print(a,id(a))
print(s,id(s))
b = s.lower()
print(b,id(b))
print(s,id(s))
print(b == s)
print(b is s)

s2 = 'Hello,Python'
print(s2.swapcase())
print(s2.capitalize())

s3 = 'i love you'
print(s3.title())



#字符串内容对齐操作的方法
#center():居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
#ljust():左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
#rjust():右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个参数是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串
#zfill():右对齐，左边用0填充，该方法只接受一个参数，用于指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身

s = 'hello,Python'
print(s.center(20,'*'))

print(s.ljust(20,'*'))
print(s.ljust(10))
print(s.ljust(20))

print(s.rjust(20,'*'))
print(s.rjust(10))
print(s.rjust(20))

print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8))  #负号前添加0

#字符串劈分操作的办法
#split():从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
#        :以通过参数sep指定的劈分字符串是劈分符
#        :通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的字串会单独做为一部分
#rsplit()::从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
#        :以通过参数sep指定的劈分字符串是劈分符
#        :通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的字串会单独做为一部分

s = 'hello world python'
lst = s.split()
print()
s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))

print(s.rsplit())
print(s1.rsplit('|'))   #也可以直接这样写，无需sep
print(s1.rsplit(sep='|',maxsplit=1))

#字符串的判断操作
#isidentifier(): 判断指定的字符串是不是合法的标识符
#isspace(): 判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
#isalpha(): 判断指定的字符串是否全部由字母组成
#isdecimal(): 判断指定的字符串是否全部由十进制的数字组成
#isnumeric(): 判断指定的字符串是否全部由数字组成
#isalnum(): 判断指定的字符串是否全部由字母和数字组成

s = 'hello,Python'
print('1.',s.isidentifier())                   #False
print('2.','hello'.isidentifier())             #True
print('3.','zhangsan'.isidentifier())          #True
print('4.','zhangsan_123'.isidentifier())      #True

print('5.','\t'.isspace())                     #True

print('6.','abc'.isalpha())                    #True
print('7.','kaixuan'.isalpha())                #True
print('8.','kaixuan1'.isalpha())               #False

print('9.','123'.isdecimal())                  #True
print('10.','123four'.isdecimal())             #False
print('11.','II II'.isdecimal())               #False

print('12.','123'.isnumeric())                 #True
print('13.','123four'.isnumeric())             #False
print('14.','II II'.isnumeric())               #False

print('15.','abc1'.isnumeric())                #False
print('16.','kaixuan123'.isnumeric())          #False
print('17.','abc!'.isnumeric())                #False
#补充：在pycharm中，中文算字母，中文表示数字的一二三四，或繁体的数字即算字母也算数字


#字符串替换：replace()：第一个参数指定被替换的字串，第二个参数指定替换字串的字符串，该方法返回替换后得到的字符串，
#                       替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
#字符串合并：join()：将列表或元组中的字符串合并成一个字符串

s = 'hello,Python'
print(s.replace('Python','Java'))
print(s,id(s))
s1 = 'hello,Python,Python,Python'
print(s1.replace('Python','C#',2))
print(s1,id(s1))

lst = ['hello','python','java']
print('|'.join(lst))
print(''.join(lst))
print(lst,id(lst))

t = ('hello','Python','C#')
print(''.join(t))
print(t,id(t))

print('*'.join('Python'))  #把python字符串看作字符串序列