
import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

slowo = input("What is the word?").upper()
nato_alpa = [phonetic_dict[letter] for letter in slowo]
print(nato_alpa)
