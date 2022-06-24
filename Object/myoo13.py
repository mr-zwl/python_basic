# 测试 重写object 的 __str__() 方法
class Person:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "名字是：{0}".format(self.name)
p = Person("张三")
print(p)  