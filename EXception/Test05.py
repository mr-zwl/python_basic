"""
自定义异常
以及抛出自定义异常
    raise 异常对象
 定义学生类， 私有属性gender, 提供对应的设置值以及访问值的方法
class 自定义异常（BaseException）:
    def __init__(self)：
"""
# 定义一个异常类
class GenderException(Exception):
    def __init__(self):
        super().__init__()
        self.errMsg = '性别只能设置成男或女'
class Student():
    def __init__(self,name,gender):
        self.name = name
        #self.__gender = gender
        self.setGender(gender)
    # 设置性别以及获取性别的方法
    # 设置性别
    def setGender(self,gender):
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            raise GenderException()
    # 获取性别
    def getGender(self):
        return self.__gender
    def showInfo(self):
        print("我叫%s 性别： %s "%(self.name,self.__gender))
try:
    stu = Student("张三","12312")
except Exception as e:
    print(e.errMsg)
# try:
#     stu.setGender("人妖")
# except GenderException as  e:
#     print(type(e))
#     print(e.args)
#     print(e.errMsg)
# stu.showInfo()
