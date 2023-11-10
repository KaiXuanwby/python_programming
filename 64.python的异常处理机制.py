#traceback模块：使用traceback模块可以用于打印异常的信息

#print(10/0)
import  traceback
def new_func():
    traceback.print_exc()

try:
    print('--------------------')
    print(1/0)
except:
    new_func()

