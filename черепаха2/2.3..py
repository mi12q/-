import turtle as t

t.shape('turtle')

dt = 0
x = 0
y = 0
ay = -9.81
Vx = 20
Vy = 50

t.shape('circle')
t.speed(0)
t.goto(-1000,0)
t.goto(+1000,0)
t.goto(0,0)
t.speed(1)

while Vx > 0.02 :

    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    t.speed((Vx**2+Vx**2)**(1/2))
    if (y < 0 and Vy < 0):
        Vy = abs(Vy)*(0.75)
        Vx = Vx*0.5
        x-= Vx * dt
        t.goto(x,0)


    else:
        t.goto(x, y)

    dt += 0.001
t.done()