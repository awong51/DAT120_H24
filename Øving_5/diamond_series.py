#importing turtle
import turtle

#assigning values and finding hypotinuse 
distance = 30
amount = 5 #input('How many diamonds')
hypo = ((distance**2)*2)**0.5

#setting up turtle and putting it on the right angle for diamonds 
t = turtle.Turtle()
t.speed('fastest')
t.lt(135)

#defining square function
def square(distance):
    for i in range(4):
        t.forward(distance)
        t.lt(90)

#drawing the diamonds. Going from the largest to the smallest so color can be filled without overlapping over the last itteration 
for i in range(1,amount+1):
    t.penup()
    t.goto(distance*i,0)
    t.pendown()
    square(hypo*i)

turtle.done()