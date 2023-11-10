# coding=gbk
# abspath           ���ڻ�ȡ�ļ���Ŀ¼�ľ���·��
# exists(path)      �����ж��ļ���Ŀ¼�Ƿ���ڣ�������ڷ���True���򷵻�False
# join(path,name)   ��Ŀ¼��Ŀ¼���ļ���ƴ������
# splitext()        �����ļ�������չ��
# basename(path)    ��һ��Ŀ¼����ȡ�ļ���
# dirname(path)     ��һ��·������ȡ�ļ�·�����������ļ���
# isdir(path)       �����ж��Ƿ�Ϊ·��
import os
import os.path
print(os.path.abspath('demo11.py'))
print(os.path.exists('demo11.py'),os.path.exists('demo1888.py'))
print(os.path.join('D:\\Python','demo11.py'))
print(os.path.split('D:\\Python\\pychram\\chap15\\demo11.py'))  # ����ļ�·�����ļ�����
print(os.path.splitext('demo11.py'))
print(os.path.basename('D:\\Python\\pychram\\chap15\\demo11.py'))
print(os.path.dirname('D:\\Python\\pychram\\chap15\\demo11.py'))
print(os.path.isdir('D:\\Python\\pychram\\chap15\\demo11.py'))


# os.walk()��ʹ���Լ����·������Ŀ¼���ļ������

path = os.getcwd()
lst_files = os.walk(path)     # os.walk()������Ҫ����ɨ��ĳ��ָ��Ŀ¼������������Ŀ¼���ļ�
print(lst_files)              # ��һ������������
for dirpath , dirname , filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('--------------------------')
    print()
    print()
    print('��ʼ����Ŀ¼�����������')
    for dire in dirname:
        print('���·���µ��ļ�����:')
        print(os.path.join(dirpath, dire))     # ���·���µ��ļ�����
    for file in filename:
        print('���·���µ��ļ���:')
        print(os.path.join(dirpath, file))    # ���·���µ��ļ���

    print('------------------------------')
