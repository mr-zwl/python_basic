# 测试参数的传递
# 传递可变对象  字典、列表、集合、自定义的对象
a = [10,20]
print(id(a))
print(a)
print("**************************************")
def test01(m):
    print(m)
    m.append(30)
    print(id(m))

test01(a)
print(a)

# 传递不可变对象的引用  int、float、字符串、元组、布尔值、function
b = 1000
print(id(b))
print(b)
print("**************************************")
def test02(n):
    n = n+2000
    print("n:",id(n))
    print(n)
test02(b)
print("a:",id(a))


