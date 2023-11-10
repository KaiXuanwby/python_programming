#转义字符即，反斜杠\+想要实现的转义功能的首字母
#为什么需要转义字符？
#当字符串中含有反斜杠，单引号，双引号等有特殊用途的字符时，必须要使用反斜杠对这些字符进行转义（转换含义）
#如：反斜杠：//    单引号：/'  双引号/""
#当字符串中包含换行符，水平制表符，退格符，回车等无法直接表示的字符时，也可以使用转义字符
#换行：/n    回车：/r    水平制表符：/t   退格：/b
#    newline     return           tab          back

print('hello\nworld')

print('hello\tworldooooo')
print('helloooo\tworld')#进行制表符\t时，四个字符做一个制表位，如果在\t前不够四个，就补齐，够四个，就空出一个制表符（四个空格）
print('helloooop\tworld')#该版本输入时，\t前若够一个制表位，则空八个空格

print('hello\rworld')#\r，即将光标回到开头，可以理解为覆盖

print('hello\bworld')#\b，退一个格，将“o”退去

print('hello\\world')
print('hello\\\\world')
print('hello\\\world')

print('say \'you are juanwang\'')#原字符，不希望字符串中的转义字符起作用，就使用原字符，即在字符串之前加上r,或R

print(R'say \'you are juanwang\'')
print(r'say \'you are juanwang\'')
#注意事项
#最后一个字符不可以是反斜杠
#print('hello\\world\')