# 测试递归函数的基本原理

def test01(n):
    print("test01",n)
    if n==0 :
        print("##OVER##")
    else:
        test01(n-1)
test01(10)

