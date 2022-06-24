# nonlocal global声明外层局部变量
a = 100
def outer():
    b = 10
    def inner():
        nonlocal b # 声明外部函数的局部变量
        print("inner:",b)
        b = 20
        global  a # 声明全局变量
        a = 100000
    inner()
    print("outer:",b)
outer()
print("a:",a)