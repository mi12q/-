import turtle

turtle.shape('turtle')
n = 100
l = 5
for i in range(n):
    turtle.forward(l)
    turtle.right(360 / n)

turtle.done()