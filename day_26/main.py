file1 = open("file1.txt", "r")
file1 = file1.readlines()

file2 = open("file2.txt", "r")
file2 = file2.readlines()

results = [int(x) for x in file1 if x in file2]
print(results)
