from turtle import Screen, Turtle
from padle import Paddle
screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")

right_position = (350,0)
left_position = (-350,0)

r_paddle = Paddle(right_position)
l_paddle = Paddle(left_position)

screen.tracer()
game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()