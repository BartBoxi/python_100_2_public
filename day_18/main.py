
import turtle as t
from turtle import *
from turtle import Screen
from random import randint
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(100):
    tim.color(random_color())
    tim.speed(randint(0, 50))
    tim.pensize(10)
    tim.goto(randint(-360, 360), randint(-360, 360))



screen = Screen()
screen.exitonclick()
