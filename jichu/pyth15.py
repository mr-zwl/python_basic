# 嵌套函数 内部函数
# 在函数内部定义的函数叫嵌套函数
def outer():
    print("outer running")
    def inter():
        print("inter running")
    inter()
# 外部无法调用内部的函数 ， 内部函数常常用来封装隐藏
# 贯彻DRY（Don't Repeat Youself） 嵌套函数 在函数内部避免重复代码
# 闭包
outer()

# def ChinaName(name,familyName):
#     print("{0} {1}".format(familyName,name))
# def EnglishName(name,familyName):
#     print("{0} {1}".format(name,familyName))
def printName(isChine,name,familyname):
    def inner_print(a,b):
        print("{0}{1}".format(a,b))
    if isChine:
        inner_print(familyname,name)
    else:
        inner_print(name,familyname)
printName(True,"文龙","赵")
printName(False,"kril","skyler")
