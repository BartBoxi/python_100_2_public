# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan")
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
#
from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)