# easy level got 10 attempts
# hard level got 5 attempts

#generate random number
# say if it's too high or too low
# two levels
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

from art_2 import logo
print(logo)


def check_answer(player_number,number, attempts):
    """Check answer againts guess. Returns the number of turns remaining"""
    if player_number > number:
        print("Too high.")
        return attempts -1
    elif player_number < number:
        print("too low")
        return attempts -1
    else:
        print(f"You got it! The answer was {number}.")


def set_difficulty():
    level = input("Chose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS




def game():
    game_is_over = False
    print("Welcome to the guessing game")
    print("I'm thinking of the number between 1 and 100")

    number = randint(1,100)
    print(number, "this is the answer")

    attempts = set_difficulty()

    player_number = 0
    while player_number != number:
        print(f"Your remaning attempts are {attempts}")
        player_number = int(input("Guess the number: "))
        attempts = check_answer(player_number, number, attempts)
        if attempts == 0:
            print("You lost! The game is over")
            return
        elif player_number != number:
            print("Try again!")
#Track the number of turns and reduce by 1 if they get it wrong

game()







