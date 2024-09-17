import math 
import turtle

#user input for length and angle in radians
'''x = float(input("Skriv lengden til x\n"))
thetaDegree = int(input("Skriv grader til theta\n"))'''

x = 50
thetaDegree = 225
#finds value for hypo, opp, theta and theta in degrees
theta = math.radians(thetaDegree)
mot = x*math.tan(theta)
hypo = (x/math.cos(theta))
thetaDegree = math.degrees(theta)
print(f'{thetaDegree} thetaDegree')
print(f'{mot} mot')
print(f'{hypo} hypo')

#turtle screen size
sc = turtle.Screen()
sc.setup(800,800)

#turtle movement
t = turtle.Turtle()
t.lt(thetaDegree)
t.forward(hypo)
t.lt(180 - (90 - thetaDegree))
t.forward(mot)
t.goto(0,0)



turtle.done()