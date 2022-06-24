# 测试 @property 的最简化方式
'''
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("录入错误！薪水要在1000 ~ 50000 之间")

emp1 = Employee("张三",30000)
print(emp1.get_salary())
emp1.set_salary(2000)
print(emp1.get_salary())
'''
class Employee:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误！薪水要在1000 ~ 50000 之间")
emp1 = Employee("张三",30000)
print(emp1.salary)

emp1.salary = -1000
print(emp1.salary)

emp1.salary = 20000
print(emp1.salary)