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


screen.tracer()
game_is_on = True
while game_is_on:
    screen.update()
    ball.sety(ball.ycor() + 5)
    ball.setx(ball.xcor() + 5)




screen.exitonclick()