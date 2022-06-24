# 多态， 同一个方法调用由于对象不同可能产生不同的行为

class Man:
    def eat(self):
        print("饿了，该吃饭了")
class Chinaese(Man):
    def eat(self):
        print("中国人吃饭用筷子")
class English(Man):
    def eat(self):
        print("英国人吃饭用叉子")
class Indian(Man):
    def eat(self):
        print("印度人吃饭用右手")

def manEat(m):
    if isinstance(m,Man):
        m.eat()
    else:
        print("不能吃饭")
manEat(Chinaese())
manEat(English())
