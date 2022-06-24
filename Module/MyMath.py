"""
自定义一个模块
    实现数学的四则运算
    两个数的加减乘除运算
"""
# 手动添加全局变量 __all__ 之后，from 模块 import * 将不在是 默认导入所有的功能，而是默认导入列表中添加的功能 (python3 不提倡使用)
__all__ = ['add','sub','mul','div']
def add(a,b):
    '''
    加法运算
    :return: 两个数的和
    '''
    return  a + b
def sub(a,b):
    '''
    减法运算
    :return:  连个数的差
    '''
    return a - b
def mul(a,b):
    '''
    乘法运算
    :return: 两个数的积
    '''
    return a * b
def div(a,b):
    '''
    除法运算
    :return:两个数的商
    '''
    return a / b
if __name__ == '__main__': # 当前模块执行

    a = 10
    b = 2
    print("和： %g"%add(a,b))
    print("差： %g"%sub(a,b))
    print("商： %g"%mul(a,b))
    print("积： %g"%div(a,b))

    # __main__
    print(__name__)