list = ['lihao','zhangsan','lisi']

# 查找元素
index = list.index('lihao')
print(index)

# 修改
list[0] = 'leeho'
print(list)

# 增
# 在指定的下标，插入一个元素
list.insert(0,'lapland')
print(list)

# 在指定的下标，插入一个元素
list.insert(0,'lapland')
print(list)

# 追加一个元素，添加到最后
list.append('leehoisleeho')
print(list)

# 追加到数据容器
list.extend(['1','2',3])
print(list)

# 删除
del list[0]
print(list)

# pop有个返回值，是被删除的元素
val = list.pop(0)
print(list)
print(val)

