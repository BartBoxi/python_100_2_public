# import colorgram
# rgb_colors = []
# colors = colorgram.extract('picture.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)


import turtle as t
from turtle import *
from turtle import Screen
from random import randint
import random

tim = t.Turtle()
t.colormode(255)


color_list = [(236, 235, 240), (236, 231, 234), (222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223),
 (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36),
 (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241),
 (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33),
 (170, 203, 205), (223, 178, 169)]
x = 0
y = 0

# t.setheading(225)
# t.forward(300)
# t.setheading(0)
#10x10 size of the cirlce is 20 and separated by 50 from each other
for _ in range(10):
    t.up()
    t.setheading(225)
    t.forward(500)
    t.setheading(0)
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.up()
        t.fd(50)
    y += 50
    t.goto(x, y)





screen = Screen()
screen.exitonclick()