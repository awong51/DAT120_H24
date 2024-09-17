import turtle 

t = turtle.Turtle()
t.speed('fastest')
t.penup()
t.goto(0,300)
t.pendown()
def sekskant(lengde):
    for i in range(6):
        t.forward(lengde)
        t.rt(60)

antall_sekskanter = 70
lengde = 6 

for i in range(antall_sekskanter):
    sekskant(lengde)
    t.rt(120)
    t.forward(lengde)
    t.lt(60)
    t.forward(lengde)
    t.lt(60)


turtle.done()