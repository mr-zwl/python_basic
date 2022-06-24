"""
try:

except: 异常1
except: 异常2
except: 异常3

except (Exception,ValueError,ZeroDivisionError)
使用 元组存储多个异常的时候，多个异常之间没有顺序要求
"""

a = input("请输入被除数：")
b = input("请输入除数")
try:
    a = int(a)
    b = int(b)
    # 求商
    c = a / b
    print("商为:%g" % c)
# except IOError:
#     print("IO异常")
# except ValueError:
#     print("数据类型有误")
# except ZeroDivisionError:
#     print("除数不能为0")
# except Exception:
#     print("未知异常")
except (Exception,ValueError,ZeroDivisionError) as e :
    print(type(e))
    print(e.args)
    print("遇到异常")
