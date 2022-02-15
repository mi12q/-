import turtle as t
from random import *


t.shape('turtle')
t.color('red')
t.speed(10)

while True:
    t.right(randint(1,360))
    t.forward(randint(1,50))


t.done()
