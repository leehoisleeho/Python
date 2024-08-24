class Person:
    name = None

    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print(f'大家好，我是{self.name}')


class Student(Person):
    grade = None

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def sayHi(self):
        super().sayHi() # 调用父类的方法
        print(f'大家好，我是{self.name},我来自{self.grade}')


stu = Student('li hao', '三年二班')
stu.sayHi()
