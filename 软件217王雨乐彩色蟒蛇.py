import turtle as t
from time import*
t.setup(1000, 1000)
t.penup()
t.fd(-200)
t.pendown()
colors = ['red', 'pink', 'green', 'blue']
t.pensize(20)
for i, color in zip(range(4), colors):
    t.pencolor(color)
    t.circle(-40, 80)
    t.circle(40, 80)
t.circle(40, 40)
t.fd(30)
t.circle(16, 100)
t.fd(30)
sleep(10)

