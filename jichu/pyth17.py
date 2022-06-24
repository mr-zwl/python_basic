# LEGB 规则
'''
python在查找 “名称” 时 按照 LEGB 规则查找的   Local --> Enclosed --> Global --> Built in

'''
# 测试LEGB
print(type(str))
#str = "global str"
def  outer():
    def inner():
        str = 'inner'
        print(str)
    inner()
outer()