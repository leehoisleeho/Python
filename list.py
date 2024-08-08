list = ['lihao','zhangsan','lisi']

# 查找元素
index = list.index('lihao')
print(index)

# 统计元素出现的次数
count = list.count('lihao')
print(count)

# 列表的长度
length = len(list)
print(length)

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

# 从前到尾 搜索到的第一个
list.remove('leeho')
print(list)

# 清空列表
list.clear()
print(list)


