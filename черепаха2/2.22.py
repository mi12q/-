import turtle as t
import math

t.shape('turtle')
t.color('blue')
t.width(3)
t.pu()
t.goto(-300,0)
t.pd()

def up():
    x = t.xcor()
    y = t.ycor()
    t.goto(x,y+50)
def right():
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50,y)
def left():
    x = t.xcor()
    y = t.ycor()
    t.goto(x-50,y)
def down():
    x = t.xcor()
    y = t.ycor()
    t.goto(x,y-50)
def diag1():
    x = t.xcor()
    y = t.ycor()
    t.goto(x+50,y+50)
def diag2():
    x = t.xcor()
    y = t.ycor()
    t.goto(x-50,y-50)

zero = ['d','d','r','u','u','l','r']
one = ['pu','d','pd','d1','d','d','u','u']
three = ['r','d2','r','d2','d1','l','d1']
four = ['d','r','d','u','u']
five = ['d','r','d','l','r','u','l','u','r']
six = ['pu','r','pd','d2','d','r','u','l','d1']
seven = ['r','d2','d','u','d1']
eight = ['d','d','r','u','l','r','u','l','r']
nine = ['d','r','d2','d1','u','l','r']

def draw(list):
    count = 0
    for i in list:
        if (i == 'r'):
            right()
        if(i == 'l'):
            left()
        if(i == 'u'):
            up()
        if(i == 'd'):
            down()
        if (i == 'd1'):
            diag1()
        if (i == 'd2'):
            diag2()
        if (i == 'pu'):
            t.penup()
        if (i == 'pd'):
            t.pendown()

        count += 1
        if count == (len(list)):
            t.penup()
            right()
            t.pendown()

def draw_element(n):
    if n == 0:
        draw(zero)
    if n == 1:
        draw(one)
    if n == 2:
        draw(two)
    if n == 3:
        draw(three)
    if n == 4:
        draw(four)
    if n == 5:
        draw(five)
    if n == 6:
        draw(six)
    if n == 7:
        draw(seven)
    if n == 8:
        draw(eight)
    if n == 9:
        draw(nine)

list = [1,4,1,7,0,0]
for i in list:
    draw_element(i)
t.done()