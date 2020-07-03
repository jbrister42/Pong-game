# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:23:19 2020

@author: jbris
"""

import turtle

wn = turtle.Screen()
wn.title("Pong by Richard")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(2)

#scoring
scorea = 0
scoreb = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Richard : 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

#Paddle A
pada = turtle.Turtle()
pada.speed(0) #sets speed to max possible speed
pada.shape("square")
pada.color("red")
pada.shapesize(stretch_wid=5, stretch_len=1)
pada.penup()
pada.goto(-350,0)

#Paddle B
padb = turtle.Turtle()
padb.speed(0) #sets speed to max possible speed
padb.shape("square")
padb.color("red")
padb.shapesize(stretch_wid=5, stretch_len=1)
padb.penup()
padb.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(1) #sets speed to max possible speed
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#function
def padaup():
    y = pada.ycor()
    y += 20
    pada.sety(y)
        
def padadown():
    y = pada.ycor()
    y -= 20
    pada.sety(y)
    
def padbup():
    y = padb.ycor()
    y += 20
    padb.sety(y)
        
def padbdown():
    y = padb.ycor()
    y -= 20
    padb.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(padaup, "w")
wn.onkeypress(padadown, "s")
wn.onkeypress(padbup, "Up")
wn.onkeypress(padbdown, "Down")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Boundaries
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        scorea += 1
        pen.clear()
        pen.write("Richard : {}  Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))
        ball.dx*=-1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        scoreb += 1
        pen.clear()
        pen.write("Richard : {}  Player 2: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "normal"))
        ball.dx*=-1
    
    #collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<padb.ycor() + 50 and ball.ycor() > padb.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<pada.ycor() + 50 and ball.ycor() > pada.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

