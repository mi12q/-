import turtle as t

t.shape('turtle')
t.speed(8)

r = 50
t.left(90)

def circles(n,r):
    for i in range(n):
        t.circle(r)
        t.right(180)
        t.circle(r)
        r = r + r/6

circles(10,30)

t.done()