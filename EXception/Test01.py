"""
1.异常
 当python 检测到一个错误时，解释器就无法继续执行下去了,反而出现一些错误提示，这就是所谓的异常
2. 案例
    需求：  输入除数与被除数   求商  并打印结果
    问题 ：
        1. str->int  如果str 不是纯数字的时候，转换出问题
        2.ZeroDivisionError: division by zero
   解决方案：
    1. 使用 if-else 增加容错处理
        业务核心  偏离
    2. 使用 异常处理方案
        try:
            可能出问题的代码
        :except
            出现问题会执行该代码块
"""
a = input("请输入被除数：")
b = input("请输入除数")
# str-> int
# 如果字符串a 和 b 都是纯数字组成，再进行转换以及后续操作
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    if b != 0:
        # 求商
        c = a / b
        print("商为:%g" % c)
    else:
        print("除数不能为0")

else:
    print("数字类型输入有误")

