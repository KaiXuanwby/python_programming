#with�������Զ�������������Դ������ʲôԭ������with�飬����ȷ���ļ���ȷ�Ĺرգ��Դ����ﵽ�ͷ���Դ��Ŀ��

print(type(open('E:/python/a.txt', 'r')))
with open('E:/python/a.txt', 'r') as file:
    print(file.read())
# ʹ�ø���������ֶ��ر��ļ�
# with֮��as֮ǰ�����ݳ�Ϊ�����ı��ʽ(open())��������һ�������Ĺ�����(open('E:/python/a.txt', 'r'))
# �����Ĺ�������һ�������ʵ����__enter__()������__exit__()����
# �뿪����ʱ�����ģ��Զ����������Ĺ����������ⷽ��__exit__()

'''
MyContentMgrʵ�������ⷽ��__enter__()��__exit__()��Ϊ������������������Ĺ�����Э��
��������ʵ�����󣬳�Ϊ�����Ĺ�����
MyContentMgr()
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter����������ִ����')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit����������ִ����')

    def show(self):
        print('show����������ִ����', 1/0)    # �������쳣ʱ��exit����Ҳ�ᱻ����


with MyContentMgr() as file:              # �൱��file = MyContentMgr()
    file.show()

# �������ļ��ĸ���
with open('E:/python/logo.png', 'rb') as src_file:
    with open('E:/python/copy2logo.png', 'wb') as target_file:
        target_file.write(src_file.read())

# �ڲ���fileʱ�����飨���룩��with��д

