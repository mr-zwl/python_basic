# lambda 表达式和匿名函数
# 实际上lambda生成了一个函数对象
# lambda表达式只允许包含一个表达式，不能包含复杂的语句，该表达式的计算结果就是函数的返回值
f = lambda a,b,c:a+b+c
print(f)
print(f(1,2,3))
g = [lambda a:a*2,lambda b:b*3,lambda c:c*3]
print(g[0](6),g[1](7),g[2](8))