# 使用递归函数，计算阶乘
def test01(n):
    if n==1:
        return 1
    else:
        return  n * test01(n-1)

print(test01(5))
