from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = (self.xcor() + self.x_move)
        new_y = (self.ycor() + self.y_move)
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

