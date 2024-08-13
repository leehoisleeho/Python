str = 'leeho'


def _length(data):
    count = 0
    for i in str:
        count += 1
    print(count)


_length(str)


# 位置参数
def user_info(name, age):
    print(f'大家好，我是{name},我今年{age}岁了')


user_info('leeho', 5)

# 关键字参数
user_info(name='leeho', age=20)


# 缺省参数
def user_info_1(age, name='leeho'):
    print(f'我是{name},今年{age}岁')


user_info_1(5)
user_info_1(5, '李浩')


# 不定长参数 args 存入元祖
def user_info_2(*args):
    print(args)


user_info_2('leeho', 5, 21)


# 存成字典，必须是key value键值对的方式传
def user_info_3(**args):
    print(args)


user_info_3(name='leeho', age=5)


# 匿名函数
def test_fun(fn):
    result = fn(1, 2)
    print(result)


def add(x, y):
    return x + y


test_fun(add)

# 定义匿名函数
# lambda关键字定义匿名函数 只能写一行，不用写return 自己也会return结果。
test_fun(lambda x, y: x + y)

