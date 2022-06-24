class Student: # 类名首字母大写，多个单词采用驼峰原则
    def __init__(self,name,score,age): #self 必须位于第一个参数
        self.name = name
        self.score = score
        self.age = age
    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))
    def say_age(self):
        print("{0}的年龄是：{1}".format(self.name,self.age))
s1 = Student("张三",235,16) # 通过类名（）调用构造函数
s1.say_score()
s1.say_age()
s2 = Student("李四",263,17)
s2.say_score()
s3 = Student("王五",211,15)
s3.say_score()


print(dir(s1)) # 输出对象的所有属性
print(s2.__dict__) # 输出定义对象的属性字典
print(isinstance(s2,Student)) #判断对象是否 指定类型
class Man:
    pass #定义空类  空语句

