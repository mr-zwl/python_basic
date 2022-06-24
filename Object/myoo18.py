# 组合  代码复用
# is-a 使用继承
# has-a 使用组合

# 使用继承实现代码的复用
class A1:
    def say_a1(self):
        print("a1")
class B1(A1):
    pass
b1 = B1()
b1.say_a1()

# 同样的效果使用组合实现代码的复用
class A2:
    def say_a2(self):
        print("a2")
class B2:
    def __init__(self,a):
        self.a = a
a2 = A2()
b2 = B2(a2)
b2.a.say_a2()

# 测试 has-a的关系，使用组合
class MobilePhone:
    def __init__(self,cpu,screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calculate(self):
        print("算你个12345")
        print("cpu对象",self)
class Screen:
    def show(self):
        print("显示一个好看的画面，亮瞎你的狗眼")
        print("screen对象",self)

m = MobilePhone(CPU(),Screen())
m.cpu.calculate()
m.screen.show()