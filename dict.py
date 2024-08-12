# 字典
my_dict = {'leeho':97,'lihao':50}
print(my_dict['leeho'])

# 定义字典
# {} dict()

# 定义重复key的字典
# 后面的不会前面的覆盖了
my_dict_1 = {'leeho':97,'lihao':50,'leeho':22}
print(my_dict_1)

# 基于key打印value
print(my_dict_1['leeho'])

# 定义嵌套字典
my_dict_2 = {
    '王力宏':{"语文":77,'数学':66,'英语':33}
}
print(my_dict_2['王力宏'])
print(my_dict_2['王力宏']['数学'])

# 新增元素
my_dict_1['lapldn'] = 33
print(my_dict_1)

# 更新
my_dict_1['lihao'] = 99
print(my_dict_1)

# 删除
my_dict_1.pop('lihao')
print(my_dict_1)

# 清空
my_dict_2.clear()
print(my_dict_2)

# 得到字典里是有的key
keys = my_dict_1.keys()
print(keys)


# 遍历字典
for item in keys:
    print(my_dict_1[item])

for item in my_dict_1:
    print(my_dict_1[item])

# 元素的数量
length = len(my_dict_1)
print(length)


