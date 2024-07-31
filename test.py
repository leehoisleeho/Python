# 打印
print('hello world')

# 注释单行注释

"""
我
是
多
行
注
释
"""

# 变量
a = 23
b = 'hello world'
type_a = type(a)

# type查看数据类型
print(type_a)
print(type(b))

"""
数据类型转换
int() str() float()
"""
num_str = str(11)  # 数字转字符串
print(type(num_str))

# 标识符
# 变量的名字 方法的名字 类的名字 等等
# 不可以使用关键字

# 运算符
# % 取余 //取整数  **平方
# 复合运算 += -= *= /= **= 等等
xxx = 2
xxx += 1

# 字符串拼接
name = 'leeho'
print('大家好我的名字叫' + name)
name_1 = '黑马程序员'
name_2 = '是对的'

# %s %d %f
# 三种不同的展位符号 分别是 字符串，数字，浮点数
msg = '学it来%s%s' % (name_1, name_2)
print(msg)

# 格式化精度控制 f'' 快速格式化
print(f'学IT来来{name_2},{name_2}')
print(f'{1-2}')

# input语句








