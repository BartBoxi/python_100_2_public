from turtle import Turtle as t
from turtle import Screen

tim = t()
i = 0
while i < 10:
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
    i += 1



screen = Screen()
screen.exitonclick()
