# 测试设计模式
# 工厂模式

class CarFactory:
    def create_car(self,brand):
        if brand == "奔驰":
            return Benz()
        if brand == "宝马":
            return BMW()
        if brand == "比亚迪":
            return BYD()
        else:
            return "未知品牌，无法创建"

class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

factory = CarFactory()
c1 = factory.create_car("奔驰")
c2 = factory.create_car("比亚迪")
print(c1,c2)
