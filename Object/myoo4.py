# 类方法是从属于 类对象的方法
# 类方法使用 测试
class Student:
    company = "ZS"
    @classmethod
    def printCompany(cls):
        print(cls.company)
Student.printCompany()
# 静态方法使用 测试
class Student2:
    company = "LS"
    @staticmethod

    def add(a,b):
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a+b
Student2.add(20,23)