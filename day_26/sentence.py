sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

sentence = sentence.split()

#word_lenght = [len(word) for word in sentence]
word_lenght = {word: len(word) for word in sentence}
print(word_lenght)
