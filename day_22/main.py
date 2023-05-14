from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")




screen.exitonclick()