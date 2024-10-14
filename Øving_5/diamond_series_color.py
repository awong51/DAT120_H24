#importing turtle
import turtle

#assigning values and finding hypotinuse 
distance = 20
amount = 25 #input('How many diamonds')
hypo = ((distance**2)*2)**0.5
colors = ["black", "gray", "magenta", "violet", "pink", "blue", "green", "yellow", "orange", "red"]

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
color = 0 
for i in reversed(range(1,amount+1)):
    t.penup()
    t.goto(distance*i,0)
    t.pendown()
    if i % 2 == amount % 2: #if conditions so that the outmost square is always colored and altering to white every other loop
        color = color % len(colors) #if color >= len(colors) then it will go "restart" the count by looping back to 0 and so it won't be a IndexError when used in colors[color]
        t.fillcolor(colors[color])
        color += 1 #only going to the next color when the one before has been used/filled
    else:
        t.fillcolor('white')
    t.begin_fill()
    square(hypo*i)
    t.end_fill()




turtle.done()