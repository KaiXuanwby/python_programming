# osģ����python���õ������ϵͳ���ܺ��ļ�ϵͳ��ص�ģ�飬��ģ���е����ִ�н��ͨ�������ϵͳ�йأ��ڲ�ͬ�Ĳ���ϵͳ������
# �õ��Ľ�����ܲ�һ��
# osģ����os.pathģ�����ڶ�Ŀ¼���ļ����в���
# os�������ϵͳ�йص�һ��ģ��

import os
os.system('notepad.exe')   # ��win+r�����ͬ
os.system('calc.exe')
# ֱ�ӵ��ÿ�ִ���ļ�
os.startfile('·��')

#��غ���
# getcwd()                          ���ص�ǰ�Ĺ���Ŀ¼
# listdir(path)                     ����ָ��·���µ��ļ���Ŀ¼��Ϣ
# mkdir(path[,mode])                ����Ŀ¼
# makedirs(path1/path2....[,mode])  �����༶Ŀ¼
# rmdir(path)                       ɾ��Ŀ¼
# removedirs(path1/path2......)     ɾ���༶Ŀ¼
# chdir(path)                       ��path����Ϊ��ǰ����Ŀ¼

import os
print(os.getcwd())
lst = os.listdir('../chap15')    # ������е�ģ���������ڲ��ҵ�Ŀ¼�£�ֱ��д�ᱨ��ʹ��../������һ��Ŀ¼
print(lst)

os.mkdir('new-dir')
os.makedirs('A/B/C')               # �����༶Ŀ¼
os.rmdir('new-dir')
os.removedirs('A/B/C')
os.chdir('D:\\Python\\pychram\\chap14')
