from turtle import Turtle
import random


class Scoreboard(Turtle):

    def __int__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score = {self.score}", align= "center")


