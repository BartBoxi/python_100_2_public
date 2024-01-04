import json

with open("saved_password.json", "r") as data_file:
    data = json.load(data_file)

data_dict = dict(data)

print(data_dict)
wartosc = input("podaj input")
password_booksy = data_dict[wartosc]['password']
print(password_booksy)