import turtle

from zmq import GSSAPI_SERVICE_PRINCIPAL_NAMETYPE

W, H = 1200, 800
WIN = turtle.Screen()
WIN.setup(width = W, height = H)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('black')
ball.penup()
ball.speed(0)
ball.goto(0, 200)
ball.dy = -2

gravity = 0.1


while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() < -350:
        ball.dy *= -1