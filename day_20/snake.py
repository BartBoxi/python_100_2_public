from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for _ in STARTING_POSITION:
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.up()
            new_snake.goto(_)
            self.snake.append(new_snake)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.snake[0].setheading(90)


    def down(self):
        if self.head.heading() !=90:
            self.snake[0].setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.snake[0].setheading(180)