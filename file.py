
"""
1.打开文件
open(name,mode,encoding)
2.读写文件
3.关闭文件
"""
import time

# f = open('test.txt','r',encoding='UTF-8')
# 读取文件
# 读取两个字符 ，不传就读取全部
# print(f.read())

# 读取文件全部行，封装到列表中
# print(f.readlines())

# 每次调用 调用一行
# print(f.readline())

# for循环读取文件
# for line in f:
#     print(line)

# 程序暂停2s
# time.sleep(2)

# 文件关闭 如果不关闭会一直被python占用。
# f.close()

# with语法
# with open 对文件进行操作，操作完以后，会自动关闭。
# with open('test.txt','r',encoding="UTF-8") as f:
#     print(f.read().count('hello'))

# 写入操作
# 打开文件
f = open('test.txt','w')
f.write('hello world\nhello python3')

# 内容刷新 前两个步骤只是把内容积攒到内存里，称为缓冲区
f.flush()

# 追加操作
f = open('test.txt','a')
f.write('\n23232')
f.flush()
f.close()
