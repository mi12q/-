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

s = []
with open('turtle.txt') as file:
    s = file.readlines()
for i in range(len(s)-1):
    s[i] = s[i].replace('\n', '')

commands = []
for list in s:
    a = list.split(',')
    commands.append(a)

zero = commands[0]
one = commands[1]
three = commands[2]
four = commands[3]
five = commands[4]
six = commands[5]
seven = commands[6]
eight = commands[7]
nine = commands[8]

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

print(s)
t.done()