import random
from turtle import Turtle as t
from turtle import *
from turtle import Screen
from random import randint
import random
tim = t()


for _ in range(100):
    colors = ["red", "purple", "brown", "pink",
              "green"]
    speed(randint(0, 50))
    pensize(25)
    pencolor(random.choice(colors))
    tim.goto(randint(-360, 360), randint(-360, 360))



screen = Screen()
screen.exitonclick()
