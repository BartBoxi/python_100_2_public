#
# try:
#     file = open("a_file.txt")
# except:
#     file = open("a_file_txt", "w")
#     file.write("Something")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters. ")

bmi = weight / height ** 2
print(bmi)
