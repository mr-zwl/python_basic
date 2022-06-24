# 浅拷贝（copy） 深拷贝（deepcopy）
# 浅拷贝：不拷贝子对象的内容、只是拷贝子对象的引用
# 深拷贝：会连子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象

# 测试浅拷贝和深拷贝
import copy
def testCopy():
    '''测试浅拷贝'''
    a = [10,20,[5,6]]
    b = copy.copy(a)
    b.append(30)
    b[2].append(7)
    print("浅拷贝。。。。")
    print("a:",a)
    print("b:",b)
def testDeepCopy():
    '''测试深拷贝'''
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)

    b.append(30)
    b[2].append(7)
    print("深拷贝。。。。")
    print("a:",a)
    print("b:",b)
testCopy()
testDeepCopy()