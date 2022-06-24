"""
package
    模块
    __init__.py
    类中的，__init__ 初始化方法
    包中的 __init__.py 初始化模块
    初始化
        首次使用包中的模块时， __init__.py ，模块会被执行一次
    __init__.py中可以存放什么？
        可以存放同普通模块一样的代码，（变量  类 函数 等都是ok ,）
        一般会写一下辅助代码，让你更方便的使用模块
            1.在测试文件中  直接 import 包
              在包的 __init__模块中导入相应模块
              import 模块
                这种方式等价于  ： 在测试文件中 使用 import 包.模块
            2. 在测试文件中
                from  包  import   *
                在 __init__ 中
                from .模块 import *
                 这种方式 等价于  ：  在测试文件中 使用 from 包   模块 import *

"""

# import Module.package1.MyMath
# import package1
# result = package1.MyMath.add(10,20)
# print(result)
from package1 import *
result = add(10,20)
print(result)
