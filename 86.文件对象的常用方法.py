#file.close()���ر��ļ����رպ��ļ������ٽ��ж�д������

#file.flush()��ˢ���ļ��ڲ����壬ֱ�Ӱ��ڲ�����������������д���ļ�, �����Ǳ����ĵȴ����������д�롣

#file.read([size])�����ļ���ȡָ�����ֽ���(size)�����δ������Ϊ�����ȡ����(��ȡ���ļ�ĩβ)��

#file.readline([size])����ȡ���У����� "\n" �ַ���

#file.readlines([sizeint])����ȡ�����в������б�������sizeint>0����������һ�ζ������ֽڣ�����Ϊ�˼����ȡѹ����

#file.seek(offset[, whence])�������ļ���ǰλ��

#file.tell()�������ļ���ǰλ�á�

#file.write(str)�����ַ���д���ļ������ص���д����ַ����ȡ�

#file.writelines(sequence)�����ļ�д��һ�������ַ����б������Ҫ������Ҫ�Լ�����ÿ�еĻ��з���

file = open('E:/python/a.txt', 'r')
# print(file.read(2))
# print(file.readline())
print(file.readlines())      # ��ȡ��һ���൱�ڹ��ָ��ָ�����һ���ַ����棬�����������������������ˣ�������հ�
file.close()

file = open('c.txt', 'a')    # a ��һ���ļ�����׷�ӡ�������ļ��Ѵ��ڣ��ļ�ָ�뽫������ļ��Ľ�β��
# file.write('hello')
lst = ['java', 'go', 'python']
file.writelines(lst)
file.close()

file = open('E:/python/a.txt', 'r')
file.seek(2)              # �����ļ���ǰλ��,�������С�ֱ�Ӵӡ������������� �����������ֽڣ�һ������ռ�����ֽ�
print(file.read())
print(file.tell())        # λ�ô�0��ʼ����
file.close()

file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
# ���ļ���д������ʱ��python����������д�룬���ǻ�д�����������ȴ����ʱд���ļ�
# flush���Ի�����������д���ļ�������ջ��������Ӷ��ﵽ����close�ļ�����д���ļ�
# ���֮������ʹ�ö��ٴ�write������ĩβд����������¸���