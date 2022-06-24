# 函数的定义和调用
def test01():
    print("*"*10)
    print("@"*10)

test01()
test01()
# 形参和实参
# ab称为形参  形参用于定义  实参用于调用
# 文档字符串用于注释   三个单引号或双引号
def printMax(a,b):
    '''用于比较两个数的大小，打印较大的值'''
    if a>b:
        print(a,"较大值")
    else:
        print(b,"较大值")
printMax(10,20)
printMax(19,13)
# 打印函数的说明
help(printMax.__doc__)

# 函数的返回值 return : 1.返回值  2.结束函数运行
def my_avg(a,b):
    '''计算两个数字的平均值'''
    return (a+b)/2
def test02():
    '''测试return后的语句不会执行'''
    print("dsfasfa")
    print("fasfasfa")
    return
    print("hello")
def test03(x,y,z):
    '''返回值改变数据类型测试 列表'''
    return [x*10,y*10,z*10]

c = my_avg(123,434)
print(c)
test02()
d = test02()
print(d) # 如果没有返回值 默认是none
print(test03(2,3,4))