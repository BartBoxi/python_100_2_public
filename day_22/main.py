import time
from turtle import Screen, Turtle
from padle import Paddle
from ball import Ball
screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
#screen.tracer()
game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update()
    ball.move()


    if ball.ycor() > 290 or ball.ycor()< -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_reset()

    if ball.xcor() < -380:
        ball.ball_reset()







screen.exitonclick()