import turtle as t

t.shape('turtle')
t.speed(0)
def square(n):
    for i in range(4):
        t.forward(n)
        t.left(90)

def squares():
    n = 10
    for i in range(10):
        square(n)
        t.penup()
        t.right(135)
        t.forward(10)
        t.left(135)
        t.pendown()
        n = n + 14
squares()
t.done()