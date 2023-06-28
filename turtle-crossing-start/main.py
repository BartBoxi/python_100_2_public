import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

STARTING_POSITION = (0, -280)

player = Player((STARTING_POSITION))
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

    #this is where i finished - how to move the cars and iterate them


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
