# 参数的类型
# 位置参数
def f1(a,b,c):
    print(a,b,c)
f1(2,3,4)
# f1(2,3)# 报错，位置参数不匹配

# 默认值参数
def f2(a,b,c=10,d=20):
    print(a,b,c,d)
f2(2,3)
f2(2,3,4)# 不传递参数的时候，会使用默认值补齐

# 命名参数
def f3(a,b,c):
    print(a,b,c)
f3(2,3,4)
f3(c=10,a=20,b=30) # 按照形式参数名，指定传递实参

# 可变参数  一个*是元组  两个*是字典
def f4(a,b,*c):
    print(a,b,c)
f4(8,9,19,20)

def f5(a,b,**c):
    print(a,b,c)
f5(8,9,name="zhangsan",age=20,socker="A")

def f6(a,b,*c,**d):
    print(a,b,c,d)
f6(2,3,'asdas','asda','asfasfadwq',name="lisi",age=18)

# 强制命名参数
def f7(*a,b,c): #第一个形式参数是数组，后边传参必须强制命名否则会全部赋值给数组
    print(a,b,c)
f7(2,4,3,b=23,c=232)