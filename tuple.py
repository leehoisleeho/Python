# 元祖 tuple
t1 = (1,2,3,4,5,6,1)

t2 = ()

t3 = tuple()

print(t1)
print(t2)
print(t3)

# 定义单个元素的元祖 要在后面加一个,
t4 = (1,)

# 元祖的操作 index的查找
index = t1.index(1)
print(index)

# count统计
c = t1.count(1)
print(c)

# 统计长度
n = len(t1)
print(n)

# while循环遍历
index = 0
while index< len(t1):
    print(t1[index])
    index += 1

print('----')

# for循环遍历
for i in t1:
    print(i)
