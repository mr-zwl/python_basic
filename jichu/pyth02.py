import turtle
t = turtle.Pen()
my_colors = ("red","green","yellow","black")
for i in range(10):
    t.width(3)
    t.speed(5)
    t.penup()
    t.goto(0,-i*50)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(50+i*50)

turtle.done()# 程序执行完，窗口仍在