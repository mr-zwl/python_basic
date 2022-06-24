# 测试函数也是对象
def test01():
    print("sfdashfvbak")
test01()
c = test01

c()
# 变量的作用域
a = 3 # 全局变量
def test02():
    b = 4 # 局部变量
    print(b*4)

test02()
print(a)
#print(b) 局部变量b 在函数test02外部 不可被使用

print(locals()) # 输出局部变量
print(globals()) # 输出全局变量