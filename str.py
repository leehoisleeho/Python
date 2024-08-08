# 字符串不可以修改的数据容器
str = 'hello world'

value = str[2]
print(value)

# index
index = str.index('h')
print(index)

# replace 替换 把字符串里面所有的 字符串1 换成 字符串2
# str(字符串1,字符串2)
str_1 = str.replace('l','2')
print(str_1)

# split 分割字符串 转为列表 接受一个参数，根据什么来分割
strList = str.split(' ')
print(strList)

# strip 规则字符串
str_2 = ' hello world    '

# 不传参数去前后的空格
print(str_2.strip())
str_3 = '12hello world21    '
print(str_3.strip('12'))

# count 统计方法
n = str.count('o')
print(n)

# 统计长度
l = len(str)
print(l)
