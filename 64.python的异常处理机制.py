#tracebackģ�飺ʹ��tracebackģ��������ڴ�ӡ�쳣����Ϣ

#print(10/0)
import  traceback
def new_func():
    traceback.print_exc()

try:
    print('--------------------')
    print(1/0)
except:
    new_func()

