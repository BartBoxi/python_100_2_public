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

def draw_spirograph(size_of_gap): #we just want to draw only the number of cirlces which can fit in the whole 360
    # degrees circle
    for _ in range(int(360 / size_of_gap)): # this is the full angle of the circle
        t.color(random_color())
        t.speed(100)
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)

draw_spirograph(7)








screen = Screen()
screen.exitonclick()
