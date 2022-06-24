class Student:
    def __init__(self, name, score):  # self 必须位于第一个参数
        self.name = name
        self.score = score


    def say_score(self):
        print("{0}的分数是：{1}".format(self.name, self.score))
stu2 = Student # 类对象

s1 = Student("张三",189)
s2 = stu2("李四",213)

s1.say_score()
s2.say_score()