import turtle as t

t.shape('turtle')
t.speed(10)

t.penup()
t.backward(300)
t.pendown()

def duga(n):
    for i in range(n):
        t.right(90)
        t.circle(50,-180)
        t.right(360)
        t.circle(10,-180)
        t.left(90)


duga(7)
t.done()
