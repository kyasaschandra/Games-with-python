"""
A simple Pong game made by watching youtube video
https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg
"""

import turtle
import winsound
import os
import random

soundpath = os.path.dirname(__file__)+"/bounce.wav"

window = turtle.Screen()
window.title("PONG by @BlitzBlaster31")
window.bgcolor("white")
window.setup(width=800,height=600)
#window.tracer(0)

# Player A
playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("black")
playerA.shapesize(stretch_wid=5,stretch_len=1)
playerA.penup()
playerA.goto(-350,0)

# Player B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("black")
playerB.shapesize(stretch_wid=5,stretch_len=1)
playerB.penup()
playerB.goto(350,0)


# Ball
ball = turtle.Turtle()
ball.speed(0.4)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = random.choice([5,-5])
ball.dy = random.choice([5,-5])

# scoring
Ascore = 0
Bscore = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {}".format(Ascore,Bscore),align="center",font=("Courier", 24, "normal"))


# Functions
def change(Ascore,Bscore):
    pen.write("Player A: {}  Player B: {}".format(Ascore,Bscore),align="center",font=("Courier", 24, "normal"))

def playsound():
    winsound.PlaySound(soundpath,winsound.SND_ASYNC)

def playerA_up():
    y = playerA.ycor()
    y+=20
    playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    y-=20
    playerA.sety(y)

def playerB_up():
    y = playerB.ycor()
    y+=20
    playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    y-=20
    playerB.sety(y)

window.listen()
window.onkeypress(playerA_up,"w")
window.onkeypress(playerA_down,"s")
window.onkeypress(playerB_up,"Up")
window.onkeypress(playerB_down,"Down")



#Main Loop
while True:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Check
    if playerA.ycor() < -250:
        playerA.sety(-250)

    if playerA.ycor() > 250:
        playerA.sety(250)
    
    if playerB.ycor() < -250:
        playerA.sety(-250)

    if playerB.ycor() > 250:
        playerA.sety(250)

    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*= -1
        playsound()
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy*= -1
        playsound()

    if ball.xcor()> 400:
        ball.goto(0,0)
        ball.dx = random.choice([5,-5])
        ball.dy = random.choice([5,-5])
        Ascore+=1
        pen.clear()
        change(Ascore, Bscore)

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.dx = random.choice([5,-5])
        ball.dy = random.choice([5,-5])
        Bscore+=1
        pen.clear()
        change(Ascore,Bscore)

    # Bounce Collision
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < playerB.ycor() + 60 and ball.ycor() > playerB.ycor() - 60:
        ball.dx *= -1
        playsound()

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < playerA.ycor() + 60 and ball.ycor() > playerA.ycor() - 60:
        ball.dx *= -1
        playsound()
