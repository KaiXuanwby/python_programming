#file.close()：关闭文件。关闭后文件不能再进行读写操作。

#file.flush()：刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。

#file.read([size])：从文件读取指定的字节数(size)，如果未给定或为负则读取所有(读取到文件末尾)。

#file.readline([size])：读取整行，包括 "\n" 字符。

#file.readlines([sizeint])：读取所有行并返回列表，若给定sizeint>0，则是设置一次读多少字节，这是为了减轻读取压力。

#file.seek(offset[, whence])：设置文件当前位置

#file.tell()：返回文件当前位置。

#file.write(str)：将字符串写入文件，返回的是写入的字符长度。

#file.writelines(sequence)：向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

file = open('E:/python/a.txt', 'r')
# print(file.read(2))
# print(file.readline())
print(file.readlines())      # 读取完一次相当于光标指针指到最后一个字符后面，所以其他函数读不到东西了，会输出空白
file.close()

file = open('c.txt', 'a')    # a 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
# file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()

file = open('E:/python/a.txt', 'r')
file.seek(2)              # 设置文件当前位置,跳过’中‘直接从’国‘读到结束 ，跳过两个字节，一个中文占两个字节
print(file.read())
print(file.tell())        # 位置从0开始计算
file.close()

file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
# 向文件中写入数据时，python并不会立刻写入，而是会写到缓冲区，等待清空时写入文件
# flush可以缓存区的内容写入文件，并清空缓存区，从而达到不用close文件就能写入文件
# 清空之后无论使用多少次write都会在末尾写入而不是重新覆盖