import turtle as t

t.shape('turtle')
t.speed(0)

n = 10
for i in range(50):
    t.forward(n)
    t.left(90)
    n = n + 5

t.done()