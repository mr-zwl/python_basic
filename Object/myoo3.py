# 类属性的使用测试
class Student:
    company = 'ZS' # 类属性
    count = 0   # 类属性
    def __init__(self,name,score):
        self.name = name  #  实例属性
        self.score = score
        Student.count = Student.count+1
    def say_score(self):   #实例方法
        print("我的公司是：",Student.company)
        print(self.name,"的分数是：",self.score)
s1 = Student('张三',123)
s1.say_score()

s2 = Student("李四",321)
s3 = Student("王五",342)

print('一共创建了{0}个对象'.format(Student.count))