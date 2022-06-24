# 私有属性和私有方法（实现封装）
# 测试私有属性

class Employee:
    __comepany ="全体成员"
    def __init__(self,name,age):
        self.name =name
        self.__age = age  #定义私有属性
    def __work(self):  #定义私有方法
        print("努力赚钱，好好工作")
        print(Employee.__comepany)
e = Employee("张三",18)

print(e.name)
print(e._Employee__age) #输出方式  私有属性
print(dir(e))
e._Employee__work()  # 调用方式  私有方法
print(Employee._Employee__comepany)