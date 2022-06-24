'''
 问题：使用自定义模块时 一个一个导入会不会麻烦
    from 模块 import 变量 类 函数
 解决方法：
    from 模块 import *
    * 默认导入模块中所有的功能
    如果在模块中手动添加 __all__ = []  这时候 * 将不再代表所有的
    # 手动添加全局变量 __all__ 之后，from 模块 import * 将不在是 默认导入所有的功能，而是默认导入列表中添加的功能
'''

from MyMath import *
result = add(10,20)
print(result)
result = sub(10,20)
print(result)
result = mul(10,20)
print(result)
result = div(10,20)
print(result)