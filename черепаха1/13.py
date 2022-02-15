import turtle as t

t.shape('turtle')
t.speed(5)

t.color('black','yellow')
t.begin_fill()
t.circle(70)
t.end_fill()

t.penup()
t.goto(-30,90)
t.pendown()

t.color('black','blue')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(30,90)
t.pendown()

t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(0,80)
t.pendown()
t.width(7)
t.goto(0,60)

t.penup()
t.goto(-30,50)
t.pendown()
t.color('red')
t.left(270)
t.circle(30,180)

t.done()

