# easy level got 10 attempts
# hard level got 5 attempts

#generate random number
# say if it's too high or too low
# two levels
import random
from art_2 import logo
print(logo)

number = random.randrange(0, 100, 1)

level = input("what level you want to play. Easy or hard? ")

player_number = int(input("Guess the number: "))

if level == "Easy" or level == "easy":
    chances = 10
    while player_number < number:
        print()




