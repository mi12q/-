import turtle as t

t.shape('turtle')


def star(n):
    angle = 180 - 180/n
    for i in range(n):
        t.backward(100)
        t.left(angle)


star(5)

t.left(360)
t.penup()
t.forward(150)
t.pendown()

star(11)
t.done()
