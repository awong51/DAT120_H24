import turtle 

t = turtle.Turtle()
t.speed('fastest')

def sekskant(lengde):
    for i in range(6):
        t.forward(lengde)
        t.rt(60)

sekskant(60)
turtle.done()