import turtle as t
import math

t.shape('turtle')
t.speed(20)

def mnogougl(n, r):
    ugol = 360 / n
    a = r * 2 * math.sin(math.pi / n)
    t.left(90 + ugol / 2)
    for i in range(n):
        t.forward(a)
        t.left(ugol)
    t.right(90 + ugol / 2)


r = 50

for n in range(3, 13):
    mnogougl(n, r)
    t.penup()
    t.forward(30)
    t.pendown()
    r += 30



t.done()