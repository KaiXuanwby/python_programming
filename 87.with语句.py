#with语句可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，以此来达到释放资源的目的

print(type(open('E:/python/a.txt', 'r')))
with open('E:/python/a.txt', 'r') as file:
    print(file.read())
# 使用该语句无需手动关闭文件
# with之后as之前的内容称为上下文表达式(open())，其结果是一个上下文管理器(open('E:/python/a.txt', 'r'))
# 上下文管理器：一个类对象实现了__enter__()方法和__exit__()方法
# 离开运行时上下文，自动调用上下文管理器的特殊方法__exit__()

'''
MyContentMgr实现了特殊方法__enter__()和__exit__()称为该类对象遵守了上下文管理器协议
该类对象的实例对象，称为上下文管理器
MyContentMgr()
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了', 1/0)    # 当产生异常时，exit方法也会被调用


with MyContentMgr() as file:              # 相当于file = MyContentMgr()
    file.show()

# 举例：文件的复制
with open('E:/python/logo.png', 'rb') as src_file:
    with open('E:/python/copy2logo.png', 'wb') as target_file:
        target_file.write(src_file.read())

# 在操作file时，建议（必须）用with来写

