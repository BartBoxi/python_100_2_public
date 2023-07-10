#this is a first method to read the file

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#this is a second method to read file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="a") as file: #mode allows the change what you can do with file w =write a=append
#     file.write("\nNew text.")
#     file.write("\nHello worlds")

with open("new_file.txt", mode="w") as file:
    file.write("\nHello worlds")