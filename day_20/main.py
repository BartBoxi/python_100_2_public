from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#body - three squares starting at 0.0 coordinate

x_position = [-40, -20, 0]
snake = []
for _ in range(0,3):
    new_snake = Turtle(shape="square")
    new_snake.color("white")
    new_snake.up()
    new_snake.goto(x=x_position[_], y = 0)
    snake.append(new_snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(snake)-1, 0, -1):
        new_x = snake[i -1].xcor()
        new_y = snake[i -1].ycor()
        snake[i].goto(new_x, new_y)
    snake[0].forward(20)
    snake[0].left(90)
    snake[0].forward(10)

screen.exitonclick()