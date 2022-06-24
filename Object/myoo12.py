# 类成员的继承和重写
# 成员继承： 子类继承了父类的构造方法外的所有成员
# 方法重写 ： 子类可以重新定义父类中的方法，这样会覆盖父类的方法，也称重写

# 测试重写
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # 私有属性
    def say_age(self):
        print("我的年龄:",self.__age)
    def say_introduce(self):
        print("我的名字是{0}".format(self.name))
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age) # 必须显示的调用父类初始化方法，不然解释器不会调用
        self.score = score

    def say_introduce(self):
        '''重写了父类的方法'''
        print("报告老师，我的名字是{0}".format(self.name,))
    def say_score(self):
        print("我的分数是：",self.score)

s = Student("张三",18,250)
s.say_age()
s.say_introduce()
s.say_score()