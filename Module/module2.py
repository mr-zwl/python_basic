"""
如何使用模块
    自定义模块
    导入模块：
        1、import 模块名1，模块2······
        导入之后如何使用？
        模块名.函数(参数)
        模块名.类
        模块名.变量

        2.导入模块中相关的数据
            form 模块 import 变量，函数，类
        导入之后如何使用？
        可以直接使用

"""
# 1、导入模块的方式
# import  random
# random.randint(1,6)
# result = random.randint(1,6)
# print(result)
# 2、导入模块中相关数据的方式
from random import randint

result = randint(1,8)
print(result)


