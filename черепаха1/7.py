import turtle as t
import math

t.shape('turtle')
t.speed(0)

def spiral_of_archimedes(n,a,b):
    ugol = 0
    while ugol < n*2*math.pi:
        r = a + b*ugol
        x = r*math.cos(ugol)
        y = r*math.sin(ugol)
        t.goto(x,y)
        ugol += 0.1

spiral_of_archimedes(10,0,1)
t.done()