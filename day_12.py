################### Scope ####################

enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
#   increase_enemies()
#   print(f"enemies outside fuction: {enemies}")

#global variable just do it outside function - thats it


# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)
#
# drink_potion()
# print(potion_strength)

#global function

#there is no block scope in python

game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)

  #to remeber if the var is within function it wont be available outside of it