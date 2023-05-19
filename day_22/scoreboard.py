from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.hideturtle()
        self.up()
        self.color("white")
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))






    def l_point(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()


