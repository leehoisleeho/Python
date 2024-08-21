"""

"""

# 导入内部模块
# import time
# f = time.localtime()
# print(f'{f.tm_year}年 {f.tm_hour}:{f.tm_min}:f{f.tm_sec}')

# 导入模块具体方法
# from time import sleep
#
# sleep(2)
#
# print(2)

# *代表全部
# from time import *
# f = localtime()
# print(f'{f.tm_year}年 {f.tm_hour}:{f.tm_min}:f{f.tm_sec}')

# as 别名
import time as shijian

# 引入自己的模块
# import module
# module.console(123)

from module import console

console('hello world')

# __all__ = ['方法名'] 在import * 的时候 ,就只能导入__all__里面这只的方法。

import my_module.module
from my_module import module

my_module.module.log(123)
module.log(1231231)