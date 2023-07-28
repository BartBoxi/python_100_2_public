#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

letter = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "rt")
letter = letter.read()

names = open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r")
new_names = names.readlines()

for name in new_names:
    stripped_i = name.strip()
    new_letter = letter.replace("[name]", stripped_i)
    with open(f"./Output/ReadyToSend/letter_for_{stripped_i}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)