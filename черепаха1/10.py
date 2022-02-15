import turtle as t


t.shape('turtle')
t.speed(10)

for i in range(3):
    t.circle(40)
    t.right(180)
    t.circle(40)
    t.left(60)

t.done()