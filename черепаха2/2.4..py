from random import randint
import turtle


number_of_turtles = 15
steps_of_time_number = 1000




pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-190, 190), randint(-190, 190))


turtle.speed(0)
turtle.pu()
turtle.goto(-200,-200)
turtle.pd()
turtle.goto(200,-200)
turtle.goto(200,200)
turtle.goto(-200,200)
turtle.goto(-200,-200)
turtle.pu()
turtle.goto(0,0)
turtle.pd()




for i in range(steps_of_time_number):
    angle = 0
    for unit in pool:
        a = 2
        if i == 1:
            angle += randint(0,180)
            unit.left(angle)
        unit.shape('circle')
        unit.forward(a)
        if ((unit.xcor() >= 195 or unit.xcor() <= -195) or (unit.ycor() <= -195 or unit.ycor() >= 195)):
            unit.right(180-angle)
        # for j in range(len(pool)-1):
        #     if pool[j+1] != unit:
        #         p = int(unit.xcor())
        #         b = int(pool[j+1].xcor())
        #         c = int(unit.ycor())
        #         d = int(pool[j + 1].ycor())
        #         if(abs(p - b) < 10 ):
        #             unit.right(180-angle)
        #             pool[j+1].right(180)
        #         if (abs(c - d) < 10):
        #             unit.right(180-angle)
        #             pool[j + 1].right(180-angle)



turtle.done()