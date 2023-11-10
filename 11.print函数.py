#python和C语言究竟不同在哪里？有什么区别？
#python在编写代码时有什么注意事项吗？
#可以输出数字，格式为：print(数字)
print(520)
print(98.55)
#print(1314)print('gkx')
#在python代码中，一行只能有一个语句，且无需分号结尾

#可以输出字符串，格式为:print('')或print("")
print('Hello world')
print("Nice to meet you")
#print(HI)

#可以输出表达式，格式为print(操作数 运算符 操作数)
print(3+1)
print((3+1)*4)
print(3+1*4)#操作运算中，默认乘除优先于加减
#若想输出“3+1”应使用print('3+1')
print('3+1')

#以上的print都是将待输出的数输出到控制台上，print也可以将数据输入到文件里
fp=open('E:/python/text1.txt','a+')#'a+'如果文件不存在就创建，存在就在文件内容后面追加
print('Hello World',file=fp)
fp.close
#将数据输出到文件中时，注意1.所指定的盘符以及路径必须存在。2.输出函数print后应有file=XXX

#若不需要换行输出，即输出内容在一行当中
print('hello','python','kaixuan')#attention：","不可缺少

