# _call_ 方法 和 可调用对象
# 定义了 _call_ 方法的对象  被称为”可调用对象“   ，即对象可以被调用

# 测试 _call_ 方法
class SalaryAccount:
    '''工资计算类'''

    def __call__(self,salary, **kwargs):
        print("算工资了。。")
        yearSalary = salary*12
        daySalary = salary/22.5   #每月工作天数
        hourSalary = daySalary/8
        return dict(yearSalary=yearSalary,mouthsalary=salary,daySalary=daySalary,hourSalary=hourSalary)
s = SalaryAccount()
print(s(13000))