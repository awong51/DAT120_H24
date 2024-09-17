#importerer turtle og bare randint fra random bibiliotekene
import turtle 
from random import randint

#verdier for lengde av sekskanter og vindu størrelse i pixler
lengde_min = 5
lengde_max = 50
antall_sekskant = 4 
screensize = 500


#bestemmer skjerm størrelse
sc = turtle.Screen()
sc.setup(screensize,screensize)

#bestemmer variabel for turtle og øker farten 
t = turtle.Turtle()
t.speed('fastest')

#funskjon til sekskant lagd i oppg b
def sekskant(lengde):
    for i in range(6):
        t.forward(lengde)
        t.rt(60)

#loop for å tegne antall sekskanter 
for i in range(antall_sekskant):
    #gir hver sekskant en tilfeldig x og y verdi. +lengde_max og -lengde_max skal minke sjangsen sekskantene blir tegnet ut av vinduet
    x = randint(int(-1*screensize/2), int((screensize/2) - lengde_max))
    y = randint(int((-1*screensize/2) + lengde_max), int(screensize/2))
    #tar opp pennen før den går til tilfeldig x,y for å ungå streken dit 
    t.penup()
    t.goto(x,y)
    t.pendown()
    #lager en tilfeldig lengde basert på min og max gitt og bruker den i sekskant funskjonen 
    lengde = randint(lengde_min,lengde_max)
    sekskant(lengde)



turtle.done()