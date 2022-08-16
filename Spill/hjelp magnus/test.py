import turtle
import random
import time


def wall_bounce():
    wn = turtle.Screen()
    wn.tracer(0)

    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-205, -205)
    pen.pendown()
    for i in range(4):
        pen.forward(410)
        pen.left(90)


    ball = turtle.Turtle()
    ball.shape = ball.shape('circle')
    ball.color('#15d798')
    ball.penup()
    ball.speed(0)
    ball.dx = 3
    ball.dy = 2

    while True:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.xcor() > 200:
            ball.dx *= -1
        if ball.xcor() < -200:
            ball.dx *= -1
        if ball.ycor() > 200:
            ball.dy *= -1
        if ball.ycor() < -200:
            ball.dy *= -1
        
        time.sleep(0.01)
        wn.update()

def ground_bounce():

    wn = turtle.Screen()
    wn.tracer(0)

    pen = turtle.Turtle()
    pen.penup()
    pen.goto(-650, -515)
    pen.pendown()
    pen.forward(1300)


    ball = turtle.Turtle()
    ball.shape = ball.shape('circle')
    ball.penup()
    ball.speed(0)
    ball.dx = 1
    ball.dy = 0

    gravity = 0.1

    while True:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() <= -500:
            ball.dy *= -1
            print('bounce')
        
        time.sleep(0.01)
        wn.update()

user_input = input('Skriv inn hvilket program du vil kjøre:\n\n1: Ground_bounce\n\n2: Wall bounce')

if user_input == '1':
    ground_bounce()
elif user_input == '2':
    wall_bounce()
