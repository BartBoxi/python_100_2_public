from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.up()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over!", align="center", font=("Arial", 24, "normal"))



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

