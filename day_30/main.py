
try:
    file = open("a_file.txt")
except:
    file = open("a_file_txt", "w")
    file.write("Something")
