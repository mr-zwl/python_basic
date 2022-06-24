# 测试推导式
# 列表推导式
y = [x*2 for x in range(1,5)]
print(y)

y = []
for x in range(1,50):
    if x%5==0:y.append(x*2)
print(y)
cells = [(row,col) for row in range(1,10) for col in range(1,10)]
print(cells)
# 字典推导式
my_text = 'i love you, i love zwl,i love sda'
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

# 集合推导式
b = {x for x in range(1,100) if x%9==0}
print(b)

# 生成器推导式(生成元组)
# 一个生成器只能运行一次   第一次迭代可以得到数据   第二次迭代发现数据已经没有了
gnt = (x for x  in range(5))
# print(tuple(gnt))
# print(tuple(gnt))

for x in gnt: # gnt是生成器对象，生成器是可迭代对象
    print(x,end=",")
print(tuple(gnt))