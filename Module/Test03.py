"""
包的概念 ： package
        可以理解为文件夹，前提，文件包含一个 __init__.py
包的作用：
        1. 将模块归类
        2.防止模块名冲突
模块中的包，名字会产生变化
新的名字：
        包名.模块名
MyMath
package1.MyMath
包中的模块如何使用
    1.import 模块
    2. from 模块  import 变量 ，函数， 类

"""
# import  Module.package1.MyMath
# result = Module.package1.MyMath.add(10,20)
# print(result)
# import MyMath
# result = MyMath.add(10,20)

from Module.package1.MyMath import *
result = add(10,20)
print(result)