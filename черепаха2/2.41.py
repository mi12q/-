from random import randint
import turtle
import math

number_of_turtles = 15
steps_of_time_number = 1000

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-190, 190), randint(-190, 190))

turtle.speed(0)
turtle.pu()
turtle.goto(-200, -200)
turtle.pd()
turtle.goto(200, -200)
turtle.goto(200, 200)
turtle.goto(-200, 200)
turtle.goto(-200, -200)
turtle.pu()
turtle.goto(0, 0)
turtle.pd()

for i in range(steps_of_time_number):
    angle = 0
    for unit in pool:
        a = 2
        if i == 1:
            angle += randint(0, 180)
            unit.left(angle)
        unit.shape('circle')
        unit.forward(a)
        if ((unit.xcor() >= 195 or unit.xcor() <= -195) or (unit.ycor() <= -195 or unit.ycor() >= 195)):
            unit.right(180 - angle)

    for j in range(0,len(pool) - 2):
            p = (pool[j].xcor())
            b = (pool[j + 1].xcor())
            c = (pool[j].ycor())
            d = (pool[j + 1].ycor())
            distx = (p-b)**2
            disty = (c-d)**2
            dist = math.sqrt(distx + disty)

            if dist < 10:
                pool[j].right(180)
                pool[j].forward(5)
                pool[j+1].right(180)
                pool[j+1].forward(5)







turtle.done()
