from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.up()
        self.color("white")
        self.goto(0, 300)
        self.write()