from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counterclockwise():
    tim.left(10)
def clear_screen():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.listen()
screen.onkey(key="s", fun=move_backward)
screen.listen()
screen.onkey(key="a", fun=move_clockwise)
screen.listen()
screen.onkey(key="d", fun=move_counterclockwise)
screen.listen()
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
"""
W = Forwards 
S = Backwards 
A = counter-clockwise (leftwords)
D = clockwise (rightwords) 
C = clear drawing 
"""

