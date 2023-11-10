#变量的赋值操作：只是形成两个变量，实际上指向同一个对象
#浅拷贝：Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
#深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()                #创建CPU类的实例对象，赋值给cpu1和cpu2，cpu1和cpu2指向CPU类的实例对象
cpu2 = cpu1                 #赋值操作就是让变量指向这个值所在的内存空间（系统自动为这个值创建）
print(cpu1,id(cpu1))
print(cpu2,id(cpu2))

#类的浅拷贝
disk = Disk()
print(disk)
computer = Computer(cpu1,disk)
import copy
computer2 = copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#解释浅拷贝
#computer这个对象是Computer类的，内含cpu1和disk，在浅拷贝时，开辟一个新的内存空间，起名computer2
#computer2这个对象也是Computer类，但是其内部的cpu和disk没有开辟新的空间，和原来相同
#对于cpu1和disk，cpu指向CPU的实例对象（CPU()），CPU的实例对象（CPU()）再通过类指针指向CPU类
#disk指向Disk的实例对象（Disk()）,Disk的实例对象（Disk()）再通过类指针指向Disk类
#也就是说，对于computer和computer2而言，其内部的cpu和disk都是指向,相同的地方，二者的cpu均指向CPU的实例对象
#二者的disk都指向Disk的实例对象
#浅拷贝类似快捷方式，而深拷贝类似全部备份
# 有一个房间，房间里有一个水壶和一个电视
# 浅拷贝的意思是，开辟一个和原来房间大小相同的房间，房间内的水壶和电视是原来房间的一个贯通的二向投影
# 举个例子，往新建的房间里的水壶加点水，原本房间里的水壶也会加同样的水，因为他们本质上是同 一个 水壶
# 在新建的房间里打开电视，原本房间里的电视也会打开，因为他们本质上是同 一个 电视


#深拷贝
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)
#解释深拷贝
#在拷贝computer3的时候，与浅拷贝不同的是，原本二者的cpu均指向CPU的实例对象，二者的disk都指向Disk的实例对象
#在深拷贝时，拷贝出来的那个对象，连原本的实例对象（CPU()和Disk()）都拷贝了一份新的，拷贝出来的那个对象的cpu和disk
#指向新的拷贝出来的实例对象
# 有一个房间，房间里有一个水壶和一个电视
# 深拷贝的意思是，开辟一个和原来房间大小相同的房间，房间内的水壶和电视是买的和原来房间完全相同的东西（生产编号不同）
# 举个例子，往新建的房间里的水壶加点水，原本房间里的水壶不会加同样的水（不会有任何改变），因为他们本质上不是同 一个 水壶
# 在新建的房间里打开电视，原本房间里的电视不会打开，因为他们本质上不是同 一个 电视