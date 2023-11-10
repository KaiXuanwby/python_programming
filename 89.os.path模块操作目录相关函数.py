# coding=gbk
# abspath           用于获取文件或目录的绝对路径
# exists(path)      用于判断文件或目录是否存在，如果存在返回True否则返回False
# join(path,name)   将目录与目录或文件名拼接起来
# splitext()        分离文件名和扩展名
# basename(path)    从一个目录中提取文件名
# dirname(path)     从一个路径中提取文件路径，不包括文件名
# isdir(path)       用于判断是否为路径
import os
import os.path
print(os.path.abspath('demo11.py'))
print(os.path.exists('demo11.py'),os.path.exists('demo1888.py'))
print(os.path.join('D:\\Python','demo11.py'))
print(os.path.split('D:\\Python\\pychram\\chap15\\demo11.py'))  # 拆分文件路径和文件名称
print(os.path.splitext('demo11.py'))
print(os.path.basename('D:\\Python\\pychram\\chap15\\demo11.py'))
print(os.path.dirname('D:\\Python\\pychram\\chap15\\demo11.py'))
print(os.path.isdir('D:\\Python\\pychram\\chap15\\demo11.py'))


# os.walk()的使用以及输出路径和子目录或文件的组合

path = os.getcwd()
lst_files = os.walk(path)     # os.walk()方法主要用来扫描某个指定目录下所包含的子目录和文件
print(lst_files)              # 是一个迭代器对象
for dirpath , dirname , filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
    print('--------------------------')
    print()
    print()
    print('开始连接目录与迭代器对象')
    for dire in dirname:
        print('输出路径下的文件夹名:')
        print(os.path.join(dirpath, dire))     # 输出路径下的文件夹名
    for file in filename:
        print('输出路径下的文件名:')
        print(os.path.join(dirpath, file))    # 输出路径下的文件名

    print('------------------------------')
