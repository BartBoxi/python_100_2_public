from turtle import Turtle as t
from turtle import Screen

tim = t()
max_num_sides = 25
num_sides = 3
for _ in range(num_sides, max_num_sides):
    angle = 360 / num_sides
    if num_sides == 4:
        tim.pencolor("green")
    elif num_sides == 5:
        tim.pencolor("yellow")
    elif num_sides == 6:
        tim.pencolor("black")
    elif num_sides == 7:
        tim.pencolor("brown")
    elif num_sides == 8:
        tim.pencolor("gray")
    elif num_sides == 9:
        tim.pencolor("white")
    else:
        tim.pencolor("purple")

    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)
    num_sides += 1



screen = Screen()
screen.exitonclick()
