import turtle as t

t.shape('turtle')

def circle():
    for i in range(12):
        t.right(360/12)
        t.forward(100)
        t.stamp()
        t.backward(100)

circle()
t.done()