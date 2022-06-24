"""
导入自定义模块
1、 import 模块
    问题： 在导入模块的时候 模块中的代码会被执行一次
    解决方案：
        在自定义模块中：
        新增控制代码：
            if __name__ == '__main__' :
             测试代码执行
2、 from 模块 import 函数 ...
"""
# import MyMath
x = 10
y = 20
# print("和：%g"%MyMath.add(x,y))

from  MyMath import add,sub,mul
print("和为：%g"%add(x,y))