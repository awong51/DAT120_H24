import math 
import turtle

#user input for length and angle in radians
x = float(input("Skriv lengden til x\n"))
thetaDegree = int(input("Skriv grader til theta\n"))

'''x = 50
thetaDegree = 225'''

#finds value for hypo, opp, theta and theta in degrees
theta = math.radians(thetaDegree)
mot = x*math.tan(theta)
hypo = x/math.cos(theta)
thetaDegree = math.degrees(theta)
'''print(f'{thetaDegree} thetaDegree')
print(f'{mot} mot')
print(f'{hypo} hypo')'''

#turtle screen size
sc = turtle.Screen()
sc.setup(800,800)

#turtle movement
t = turtle.Turtle()
t.forward(x)
t.lt(90)
t.forward(mot)
t.lt(180 - (90 - thetaDegree)) #spins turtle 180* around and turns x degrees depending on the right angle minus the theta(in degrees) input  
t.forward(hypo)
turtle.done()