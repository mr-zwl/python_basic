'''
什么是模块
   只要以 .py 为后缀 的文件都可以被称为模块
模块中可以包含什么东西？
    1、变量
    2、函数
    3、面向对象 （类 -> 对象）
    4、可执行代码
使用模块有什么好处？
    管理方便，易维护
    降低复杂度
'''
PI = 3.14
def get_area(r):
    '''
    求圆面积的方法
    :param r: 半径
    :return: 圆的面积
    '''
    return  PI * r ** 2
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_info(self):
        '''
        展示学生信息
        :return:  None
        '''
        print("name : %s age: %d"%(self.name,self.age))
c = Student("张三",17)
c.show_info()
print(PI)
print("半径为2的圆的面积是：%g"%get_area(2))
