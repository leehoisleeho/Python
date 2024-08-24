# 设计一个类
class Student:
    name = None
    gender: None
    # 私有属性
    __names = None
    """
    __init__ 构造函数
    self 指向当前类
    """

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __test(self):
        print('我是私有属性')

    def say(self):
        print(self.__test())
        print(f'大家好，我是{self.name}')


stu_1 = Student('lee ho', '男')
print(stu_1.say())
