# 测试eval函数的使用
# 作用是将字符串str当成有效的表达式进行求值并返回计算结果
s = "print('abcdefg')"
eval(s)
a = 10
b = 20
c = eval("a+b")
print(c)
dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)
print(d)