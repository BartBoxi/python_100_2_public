
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonethic():
    slowo = input("What is the word?").upper()
    try:
        nato_alpa = [phonetic_dict[letter] for letter in slowo]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonethic()
    else:
        print(nato_alpa)
generate_phonethic()
