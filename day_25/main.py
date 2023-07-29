# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

import csv
import pandas
import numpy

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#        if row[1] != "temp":
#            temperatures.append(row[1])
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# temp_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # # print(temp_list)
# # # average = sum(temp_list) / (len(temp_list))
# # # round(average, 2)
# # # print(average)
#
# print(data["temp"].max())

# print(data.condition)

#GET data in the row

#print(data[data.day == "Monday"])
#print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# day = data[data.day == "Monday"]
# temp_celc_monday = int(day.temp)
# temp_farh_monday = (temp_celc_monday *(9/5) + 32)
# print(temp_farh_monday)


#Creating a dataframe

# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("new_data.csv")

#Getting data from Central Park

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray,black,cinnamon)

data_dict = {
    "colors": ["Gray", "Black", "Cinnamon"],
    "scores": [gray, black, cinnamon]
}

data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("colors_of_squirrels")
#print(data_per_type)
# print(data_per_type)
# gray = data[data.PrimaryFurColor == "Gray"]
# print(gray)
#print(data_per_type)


