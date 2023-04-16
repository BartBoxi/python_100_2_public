from turtle import Turtle, Screen
import random

screen = Screen()
is_race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(prompt= "Which turtle going to win?", title= "Make your bet!")
colors = ["red", "green", "pink", "blue", "purple", "black", "yellow", "grey"]
y_position = [-80, -50, -20, 10, 40, 70]
all_turtles = []
for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.up()
    new_turtle.goto(x=-230, y = y_position[_])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color ==  user_bet:
                print(f"You won. Your turtle {winning_color} won")
                is_race_on = False
            else:
                print(f"You lost. Winning turtle is {winning_color}")
                is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
