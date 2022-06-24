# @property 装饰器
# 将一个方法的调用方式 变成 “属性调用”
class  Employee:
    @property
    def salary(self):
        print("salary run...")
        return 10000
emp1 = Employee()
# emp1.salary()
print(emp1.salary)

