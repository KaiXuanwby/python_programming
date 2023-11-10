#元组没有集合生成式，因为它是不可变序列
#用于生成集合的公式：{i*i for i in range(1,10)}
#{表示集合的元素表达式  for  自定义变量  in  可迭代对象}
#将{}修改为[]就是列表生成式

#列表生成式
lst = [ i*i for i in range(10)]
print(lst)

#集合生成式
lst = [ i*i for i in range(10)]
print(lst)

