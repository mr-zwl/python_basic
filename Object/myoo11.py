# 面向对象三大特征
'''
封装 （隐藏）
  隐藏对象的属性和实现细节，只对外提供必要的方法 将“细节封装起来” ，只对外暴露 “相关调用方法”

继承
  继承让子类具有父类的特性，提高代码的复用性
  从设计上是一种增量进化
多态
  同一种方法调用由于对象不同 会产生不同的行为
'''

# 测试继承的基本使用
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def say_age(self):
        print("年龄，！！！")
class Student(Person):
    def __init__(self,name,age,score):
        Person.__init__(self,name,age) # 继承父类的属性
        self.score = score

# Student --> Person --> object
print(Student.mro())

s = Student("张三",18,60)
s.say_age() # 父类的方法子类可以直接用
print(s.name)
print(dir(s))
print(s._Person__age)