# todo: "Generate a random number"
# todo: "generate a list with accounts"
# todo: "print two elements from the list and ask user which one is higher or lower for him"
# todo: "write a functionn"

#https://www.jetbrains.com/help/pycharm/using-todo.html
import random

from art import logo
from game_data import data
print(logo)

# lista = random.choice(data['name'])
# print(lista)

for person in data:
    nowa_lista = []
    nowa_lista.append(person['name'])
    nowa_lista.append(person['follower_count'])





