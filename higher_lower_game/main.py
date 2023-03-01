# todo: "Generate a random number"
# todo: "generate a list with accounts"
# todo: "print two elements from the list and ask user which one is higher or lower for him"
# todo: "write a functionn"

#https://www.jetbrains.com/help/pycharm/using-todo.html
import random

from art import logo
from game_data import data
print(logo)

#Generate a radnom account from the game

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
print(account_a)

#Format the account data into printable format

account_name = account_a["name"]
account_description = account_a["description"]
account_country = account_a["country"]

print(f"Account A is {account_name}, a {account_description} from {account_country}")

account_name_b = account_b['name']
account_description_b = account_b["description"]
account_country_b = account_b["country"]

print(f"Account B is {account_name_b}, a {account_description_b} from {account_country_b}")


#Ask user for a guess

answer = input("Guess which account got more subscribers. Account A or B? Enter 'A' or 'B' ")

#Check if user is correct

if answer == "A" and (account_a["follower_count"] > account_b["follower_count"]):
    print("You are right")
else:
    print("You are wrong")

#Get follower count of each account



# Use if statement to check if user is correct

#Score keeping

#Make the game repeatable

#Making account at position B become the next account at position A

# clear the screen between rounds









